from contextlib import contextmanager
from contextlib import nullcontext
from enum import IntEnum
from enum import auto

from pynescript.ast import types as ast
from pynescript.ast.helpers import iter_fields
from pynescript.ast.types import AST


class NodeVisitor:
    """
    A node visitor base class that walks the abstract syntax tree and calls a
    visitor function for every node found.  This function may return a value
    which is forwarded by the `visit` method.
    This class is meant to be subclassed, with the subclass adding visitor
    methods.
    Per default the visitor functions for the nodes are ``'visit_'`` +
    class name of the node.  So a `TryFinally` node visit function would
    be `visit_TryFinally`.  This behavior can be changed by overriding
    the `visit` method.  If no visitor function exists for a node
    (return value `None`) the `generic_visit` visitor is used instead.
    Don't use the `NodeVisitor` if you want to apply changes to nodes during
    traversing.  For this a special visitor exists (`NodeTransformer`) that
    allows modifications.
    """

    def visit(self, node):
        """Visit a node."""
        method = "visit_" + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for _field, value in iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)


class NodeTransformer(NodeVisitor):
    """
    A :class:`NodeVisitor` subclass that walks the abstract syntax tree and
    allows modification of nodes.
    The `NodeTransformer` will walk the AST and use the return value of the
    visitor methods to replace or remove the old node.  If the return value of
    the visitor method is ``None``, the node will be removed from its location,
    otherwise it is replaced with the return value.  The return value may be the
    original node in which case no replacement takes place.
    Here is an example transformer that rewrites all occurrences of name lookups
    (``foo``) to ``data['foo']``::
       class RewriteName(NodeTransformer):
           def visit_Name(self, node):
               return Subscript(
                   value=Name(id='data', ctx=Load()),
                   slice=Constant(value=node.id),
                   ctx=node.ctx
               )
    Keep in mind that if the node you're operating on has child nodes you must
    either transform the child nodes yourself or call the :meth:`generic_visit`
    method for the node first.
    For nodes that were part of a collection of statements (that applies to all
    statement nodes), the visitor may also return a list of nodes rather than
    just a single node.
    Usually you use the transformer like this::
       node = YourTransformer().visit(node)
    """

    def generic_visit(self, node):
        for field, old_value in iter_fields(node):
            if isinstance(old_value, list):
                new_values = []
                for value in old_value:
                    if isinstance(value, AST):
                        value = self.visit(value)
                        if value is None:
                            continue
                        elif not isinstance(value, AST):
                            new_values.extend(value)
                            continue
                    new_values.append(value)
                old_value[:] = new_values
            elif isinstance(old_value, AST):
                new_node = self.visit(old_value)
                if new_node is None:
                    delattr(node, field)
                else:
                    setattr(node, field, new_node)
        return node


class Precedence(IntEnum):
    """Precedence table that originated from pinescript grammar."""

    TUPLE = auto()
    YIELD = auto()  # 'yield', 'yield from'
    TEST = auto()  # 'if'-'else', 'lambda'
    OR = auto()  # 'or'
    AND = auto()  # 'and'
    NOT = auto()  # 'not'
    CMP = auto()  # '<', '>', '==', '>=', '<=', '!=',
    # 'in', 'not in', 'is', 'is not'
    EXPR = auto()
    BOR = EXPR  # '|'
    BXOR = auto()  # '^'
    BAND = auto()  # '&'
    SHIFT = auto()  # '<<', '>>'
    ARITH = auto()  # '+', '-'
    TERM = auto()  # '*', '@', '/', '%', '//'
    FACTOR = auto()  # unary '+', '-', '~'
    POWER = auto()  # '**'
    AWAIT = auto()  # 'await'
    ATOM = auto()

    def next(self):
        try:
            return self.__class__(self + 1)
        except ValueError:
            return self


class Unparser(NodeVisitor):
    # pylint: disable=unused-argument

    def __init__(self):
        self._source = []
        self._buffer = []
        self._precedences = {}
        self._indent = 0

    def maybe_newline(self):
        """Adds a newline if it isn't the start of generated source"""
        if self._source:
            self.write("\n")

    def fill(self, text=""):
        """Indent a piece of text and append it, according to the current
        indentation level"""
        self.maybe_newline()
        self.write("    " * self._indent + text)

    def write(self, text):
        """Append a piece of text"""
        assert isinstance(text, str)
        self._source.append(text)

    def buffer_writer(self, text):
        self._buffer.append(text)

    @property
    def buffer(self):
        value = "".join(self._buffer)
        self._buffer.clear()
        return value

    @contextmanager
    def block(self):
        """A context manager for preparing the source for blocks. It adds
        the character':', increases the indentation on enter and decreases
        the indentation on exit. If *extra* is given, it will be directly
        appended after the colon character.
        """
        self._indent += 1
        yield
        self._indent -= 1

    @contextmanager
    def delimit(self, start, end):
        """A context manager for preparing the source for expressions. It adds
        *start* to the buffer and enters, after exit it adds *end*."""
        self.write(start)
        yield
        self.write(end)

    def delimit_if(self, start, end, condition):
        if condition:
            return self.delimit(start, end)
        else:
            return nullcontext()

    def require_parens(self, precedence, node):
        """Shortcut to adding precedence related parens"""
        return self.delimit_if("(", ")", self.get_precedence(node) > precedence)

    def get_precedence(self, node):
        return self._precedences.get(node, Precedence.TEST)

    def set_precedence(self, precedence, *nodes):
        for node in nodes:
            self._precedences[node] = precedence

    def traverse(self, node, sep=None):
        if isinstance(node, list):
            first = True
            for item in node:
                if first:
                    first = False
                elif sep:
                    self.write(sep)
                self.traverse(item)
        else:
            super().visit(node)

    def interleave(self, inter, f, seq):
        """Call f on each item in seq, calling inter() in between."""
        seq = iter(seq)
        try:
            f(next(seq))
        except StopIteration:
            pass
        else:
            for x in seq:
                inter()
                f(x)

    def items_view(self, traverser, items, single=False):
        """Traverse and separate the given *items* with a comma and append it to
        the buffer. If *items* is a single item sequence, a trailing comma
        will be added."""
        if isinstance(items, list):
            if len(items) == 1:
                traverser(items[0])
                if single:
                    self.write(",")
            else:
                self.interleave(lambda: self.write(", "), traverser, items)
        else:
            traverser(items)

    # Note: as visit() resets the output text, do NOT rely on
    # NodeVisitor.generic_visit to handle any nodes (as it calls back in to
    # the subclass visit() method, which resets self._source to an empty list)
    def visit(self, node):
        """Outputs a source code string that, if converted back to an ast
        (using ast.parse) will generate an AST equivalent to *node*"""
        self._source = []
        self.traverse(node)
        return "".join(self._source)

    def visit_Script(self, node: ast.Script):
        if node.version:
            self.fill(f"//@version={node.version}")
        self.traverse(node.body)

    def visit_Assign(self, node: ast.Assign):
        self.fill()
        if node.declaration_mode:
            self.traverse(node.declaration_mode)
            self.write(" ")
        if node.type_specifier:
            self.traverse(node.type_specifier)
            self.write(" ")
        if isinstance(node.target, str):
            self.write(node.target)
        else:
            self.traverse(node.target)
        self.write(" = ")
        self.traverse(node.value)

    def visit_AugAssign(self, node: ast.AugAssign):
        self.fill()
        if isinstance(node.target, str):
            self.write(node.target)
        else:
            self.traverse(node.target)
        self.write(" ")
        self.traverse(node.operator)
        self.write("= ")
        self.traverse(node.value)

    def visit_Expr(self, node: ast.Expr):
        self.fill()
        self.traverse(node.value)

    def visit_Parameter(self, node: ast.Parameter):
        self.write(node.name)
        if node.default_value:
            self.write("=")
            self.traverse(node.value)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.fill()
        self.write(node.name)
        with self.delimit("(", ")"):
            if node.parameters:
                self.items_view(self.traverse, node.parameters)
        self.write(" => ")
        if (
            len(node.body) == 1
            and isinstance(node.body[0], ast.Expr)
            and not isinstance(
                node.body[0].value, (ast.If, ast.Switch, ast.For, ast.While)
            )
        ):
            self.traverse(node.body[0].value)
        else:
            with self.block():
                self.traverse(node.body)

    def visit_Argument(self, node: ast.Argument):
        if node.name:
            self.write(node.name)
            self.write("=")
        self.traverse(node.value)

    def visit_Call(self, node: ast.Call):
        self.set_precedence(Precedence.ATOM, node.func)
        self.traverse(node.func)
        if node.type_argument:
            with self.delimit("<", ">"):
                self.items_view(self.traverse, node.type_argument)
        with self.delimit("(", ")"):
            if node.arguments:
                self.items_view(self.traverse, node.arguments)

    def visit_If(self, node: ast.If):
        self.write("if ")
        self.traverse(node.condition)
        with self.block():
            self.traverse(node.body)
        while (
            node.orelse and len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If)
        ):
            node = node.orelse[0]
            self.fill("else if ")
            self.traverse(node.condition)
            with self.block():
                self.traverse(node.body)
        if node.orelse:
            self.fill("else")
            with self.block():
                self.traverse(node.orelse)

    def visit_Switch(self, node: ast.Switch):
        self.write("switch")
        if node.expression:
            self.write(" ")
            self.traverse(node.expression)
        with self.block():
            self.traverse(node.cases)

    def visit_SwitchCase(self, node: ast.SwitchCase):
        self.fill()
        if node.expression:
            self.traverse(node.expression)
            self.write(" ")
        self.write("=> ")
        if len(node.body) == 1 and isinstance(node.body[0], ast.Expr):
            self.traverse(node.body[0].value)
        else:
            with self.block():
                self.traverse(node.body)

    def visit_For(self, node: ast.For):
        self.write("for ")
        if isinstance(node.target, str):
            self.write(node.target)
        else:
            self.traverse(node.target)
        self.write(" = ")
        self.traverse(node.initial_value)
        self.write(" to ")
        self.traverse(node.final_value)
        if node.increment_value:
            self.write(" by ")
            self.traverse(node.increment_value)
        with self.block():
            self.traverse(node.body)

    def visit_ForIn(self, node: ast.ForIn):
        self.write("for ")
        if isinstance(node.target, str):
            self.write(node.target)
        else:
            self.traverse(node.target)
        self.write(" in ")
        self.traverse(node.iterate_value)
        with self.block():
            self.traverse(node.body)

    def visit_While(self, node: ast.While):
        self.write("while ")
        self.traverse(node.condition)
        with self.block():
            self.traverse(node.body)

    def visit_Break(self, node: ast.Break):
        self.fill("break")

    def visit_Continue(self, node: ast.Continue):
        self.fill("continue")

    def visit_Ternary(self, node: ast.Ternary):
        with self.require_parens(Precedence.TEST, node):
            self.set_precedence(Precedence.TEST.next(), node.condition, node.true_value)
            self.traverse(node.condition)
            self.write(" ? ")
            self.traverse(node.true_value)
            self.write(" : ")
            self.set_precedence(Precedence.TEST, node.false_value)
            self.traverse(node.false_value)

    unary_operators = {
        "Invert": "~",
        "Not": "not",
        "UAdd": "+",
        "USub": "-",
    }

    unary_operator_precedence = {
        "not": Precedence.NOT,
        "~": Precedence.FACTOR,
        "+": Precedence.FACTOR,
        "-": Precedence.FACTOR,
    }

    def visit_Unary(self, node: ast.Unary):
        operator = self.unary_operators[node.operator.__class__.__name__]
        operator_precedence = self.unary_operator_precedence[operator]
        with self.require_parens(operator_precedence, node):
            self.write(operator)
            # factor prefixes (+, -, ~) shouldn't be seperated
            # from the value they belong, (e.g: +1 instead of + 1)
            if operator_precedence is not Precedence.FACTOR:
                self.write(" ")
            self.set_precedence(operator_precedence, node.operand)
            self.traverse(node.operand)

    binary_operators = {
        "Add": "+",
        "Sub": "-",
        "Mult": "*",
        "MatMult": "@",
        "Div": "/",
        "Mod": "%",
        "LShift": "<<",
        "RShift": ">>",
        "BitOr": "|",
        "BitXor": "^",
        "BitAnd": "&",
        "FloorDiv": "//",
        "Pow": "**",
        "Equal": "==",
        "NotEqual": "!=",
    }

    binary_operator_precedence = {
        "+": Precedence.ARITH,
        "-": Precedence.ARITH,
        "*": Precedence.TERM,
        "@": Precedence.TERM,
        "/": Precedence.TERM,
        "%": Precedence.TERM,
        "<<": Precedence.SHIFT,
        ">>": Precedence.SHIFT,
        "|": Precedence.BOR,
        "^": Precedence.BXOR,
        "&": Precedence.BAND,
        "//": Precedence.TERM,
        "**": Precedence.POWER,
        "==": Precedence.CMP,
        "!=": Precedence.CMP,
    }

    binnary_operator_rassoc = set()

    def visit_Binary(self, node: ast.Binary):
        operator = self.binary_operators[node.operator.__class__.__name__]
        operator_precedence = self.binary_operator_precedence[operator]
        with self.require_parens(operator_precedence, node):
            if operator in self.binnary_operator_rassoc:
                left_precedence = operator_precedence.next()
                right_precedence = operator_precedence
            else:
                left_precedence = operator_precedence
                right_precedence = operator_precedence.next()

            self.set_precedence(left_precedence, node.left)
            self.traverse(node.left)
            self.write(f" {operator} ")
            self.set_precedence(right_precedence, node.right)
            self.traverse(node.right)

    compare_operators = {
        "Equal": "==",
        "NotEqual": "!=",
        "LessThan": "<",
        "LessThanEqual": "<=",
        "GreaterThan": ">",
        "GreaterThanEqual": ">=",
    }

    def visit_Compare(self, node: ast.Compare):
        with self.require_parens(Precedence.CMP, node):
            self.set_precedence(Precedence.CMP.next(), node.left, *node.comparators)
            self.traverse(node.left)
            for o, e in zip(node.operators, node.comparators):
                self.write(f" {self.compare_operators[o.__class__.__name__]} ")
                self.traverse(e)

    boolean_operators = {
        "And": "and",
        "Or": "or",
    }

    boolean_operator_precedence = {
        "and": Precedence.AND,
        "or": Precedence.OR,
    }

    def visit_Boolean(self, node: ast.Boolean):
        operator = self.boolean_operators[node.operator.__class__.__name__]
        operator_precedence = self.boolean_operator_precedence[operator]

        def increasing_level_traverse(node):
            nonlocal operator_precedence
            operator_precedence = operator_precedence.next()
            self.set_precedence(operator_precedence, node)
            self.traverse(node)

        with self.require_parens(operator_precedence, node):
            s = f" {operator} "
            self.interleave(
                lambda: self.write(s), increasing_level_traverse, node.values
            )

    def visit_Equal(self, node):
        self.write("==")

    def visit_NotEqual(self, node):
        self.write("!=")

    def visit_LessThan(self, node):
        self.write("<")

    def visit_LessThanEqual(self, node):
        self.write("<=")

    def visit_GreaterThan(self, node):
        self.write(">")

    def visit_GreaterThanEqual(self, node):
        self.write(">=")

    def visit_Not(self, node):
        self.write("not")

    def visit_UAdd(self, node):
        self.write("+")

    def visit_USub(self, node):
        self.write("-")

    def visit_Add(self, node):
        self.write("+")

    def visit_Sub(self, node):
        self.write("-")

    def visit_Mult(self, node):
        self.write("*")

    def visit_Div(self, node):
        self.write("/")

    def visit_Mod(self, node):
        self.write("%")

    def visit_And(self, node):
        self.write("and")

    def visit_Or(self, node):
        self.write("or")

    def visit_Colon(self, node):
        self.write(":")

    def visit_CollectionType(self, node: ast.CollectionType):
        self.traverse(node.type_name)
        with self.delimit("<", ">"):
            self.items_view(self.traverse, node.type_argument)

    def visit_ArrayType(self, node: ast.ArrayType):
        self.traverse(node.element_type)
        self.write("[]")

    def visit_Int(self, node):
        self.write("int")

    def visit_Float(self, node):
        self.write("float")

    def visit_Bool(self, node):
        self.write("bool")

    def visit_Color(self, node):
        self.write("color")

    def visit_String(self, node):
        self.write("string")

    def visit_Label(self, node):
        self.write("label")

    def visit_Line(self, node):
        self.write("line")

    def visit_Box(self, node):
        self.write("box")

    def visit_Table(self, node):
        self.write("table")

    def visit_Linefill(self, node):
        self.write("linefill")

    def visit_Array(self, node):
        self.write("array")

    def visit_Matrix(self, node):
        self.write("matrix")

    def visit_Var(self, node):
        self.write("var")

    def visit_VarIp(self, node):
        self.write("varip")

    def visit_Constant(self, node):
        if hasattr(node.value, "__pinescript_repr__"):
            r = node.value.__pinescript_repr__()
        else:
            r = repr(node.value)
        self.write(r)

    def visit_Name(self, node: ast.Name):
        self.write(node.id)

    def visit_Attribute(self, node: ast.Attribute):
        self.set_precedence(Precedence.ATOM, node.value)
        self.traverse(node.value)
        self.write(".")
        self.write(node.attribute)

    def visit_Subscript(self, node: ast.Subscript):
        self.traverse(node.value)
        with self.delimit("[", "]"):
            self.items_view(self.traverse, node.index)

    def visit_Tuple(self, node: ast.Tuple):
        with self.delimit("[", "]"):

            def traverser(item):
                if isinstance(item, str):
                    self.write(item)
                else:
                    self.traverse(item)

            self.items_view(traverser, node.values)
