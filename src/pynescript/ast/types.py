"""Type for parsing and building AST."""

from __future__ import annotations

from abc import ABC
from collections.abc import Hashable
from typing import Sequence
from typing import Union

from pynescript.types import BoolType
from pynescript.types import ColorType
from pynescript.types import FloatType
from pynescript.types import IntType
from pynescript.types import PythonIntType
from pynescript.types import PythonStringType
from pynescript.types import StringType


# builtin types for ast

Identifier = PythonStringType
BuiltinInt = PythonIntType
BuiltinString = PythonStringType
ConstantType = Union[IntType, FloatType, BoolType, ColorType, StringType]

# ast nodes


class AST(ABC, Hashable):

    location_fields = [
        "loc",
        "end_loc",
        "lineno",
        "col_offset",
        "end_lineno",
        "end_col_offset",
    ]

    def __init__(self):
        self.loc: BuiltinInt | None = None
        self.end_loc: BuiltinInt | None = None
        self.lineno: BuiltinInt | None = None
        self.col_offset: BuiltinInt | None = None
        self.end_lineno: BuiltinInt | None = None
        self.end_col_offset: BuiltinInt | None = None

    def set_attributes(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def iter_fields(self):
        fields = list(self.__dict__.keys())
        for field in fields:
            if field not in self.location_fields:
                try:
                    yield field, getattr(self, field)
                except AttributeError:
                    pass

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __repr__(self):
        from pynescript.ast.helpers import dump

        return dump(self)

    def __hash__(self):
        return id(self)


class Script(AST):
    def __init__(
        self,
        body: Sequence[Statement],
        version: BuiltinInt | None = None,
    ):
        super().__init__()
        self.body = body
        self.version = version


class Constant(AST):
    def __init__(self, value: ConstantType):
        super().__init__()
        self.value = value


class Name(AST):
    # pylint: disable=redefined-builtin
    def __init__(self, id: Identifier):
        super().__init__()
        self.id = id


class Attribute(AST):
    def __init__(self, value: Expression, attribute: Identifier):
        super().__init__()
        self.value = value
        self.attribute = attribute


class Subscript(AST):
    def __init__(self, value: Expression, index: Expression | None = None):
        super().__init__()
        self.value = value
        self.index = index


class Tuple(AST):
    def __init__(self, values: Sequence[Expression]):
        super().__init__()
        self.values = values


class Var(AST):
    pass


class VarIp(AST):
    pass


DeclarationMode = Union[Var, VarIp]


class Int(AST):
    pass


class Float(AST):
    pass


class Bool(AST):
    pass


class Color(AST):
    pass


class String(AST):
    pass


class Label(AST):
    pass


class Line(AST):
    pass


class Box(AST):
    pass


class Table(AST):
    pass


class Linefill(AST):
    pass


class Array(AST):
    pass


class Matrix(AST):
    pass


AtomicTypeName = Union[
    Int, Float, Bool, Color, String, Label, Line, Box, Table, Linefill
]
CollectionTypeName = Union[Array, Matrix]


class CollectionType(AST):
    def __init__(
        self,
        type_name: CollectionTypeName,
        type_argument: TypeSpecifier,
    ):
        super().__init__()
        self.type_name = type_name
        self.type_argument = type_argument


class ArrayType(AST):
    def __init__(self, element_type: TypeSpecifier):
        super().__init__()
        self.element_type = element_type


TypeSpecifier = Union[CollectionType, ArrayType, AtomicTypeName]


class Add(AST):
    pass


class Sub(AST):
    pass


class Mult(AST):
    pass


class Div(AST):
    pass


class Mod(AST):
    pass


BinaryOperator = Union[
    Add,
    Sub,
    Mult,
    Div,
    Mod,
]


class Colon(AST):
    pass


AugAssignOperator = Union[
    Colon,
    Mult,
    Div,
    Mod,
    Add,
    Sub,
]


class Assign(AST):
    def __init__(
        self,
        target: Identifier | Tuple[Identifier],
        value: Expression | Structure,
        declaration_mode: DeclarationMode | None = None,
        type_specifier: TypeSpecifier | None = None,
    ):
        super().__init__()
        self.target = target
        self.value = value
        self.declaration_mode = declaration_mode
        self.type_specifier = type_specifier


class AugAssign(AST):
    def __init__(
        self,
        target: Identifier | Tuple[Identifier],
        operator: AugAssignOperator,
        value: Expression | Structure,
    ):
        super().__init__()
        self.target = target
        self.operator = operator
        self.value = value


class Parameter(AST):
    def __init__(
        self,
        name: Identifier,
        default_value: Expression | None = None,
    ):
        super().__init__()
        self.name = name
        self.default_value = default_value


class FunctionDef(AST):
    def __init__(
        self,
        name: Identifier,
        body: Sequence[Statement],
        parameters: Sequence[Parameter] | None = None,
    ):
        super().__init__()
        self.name = name
        self.body = body
        self.parameters = parameters


class Argument(AST):
    def __init__(
        self,
        value: Expression,
        name: Identifier | None = None,
    ):
        super().__init__()
        self.value = value
        self.name = name


class Call(AST):
    def __init__(
        self,
        func: Name | Attribute,
        arguments: Sequence[Argument] | None = None,
        type_argument: AtomicTypeName | None = None,
    ):
        super().__init__()
        self.func = func
        self.arguments = arguments
        self.type_argument = type_argument


class If(AST):
    def __init__(
        self,
        condition: Expression,
        body: Sequence[Statement],
        orelse: Sequence[Statement] | None = None,
    ):
        super().__init__()
        self.condition = condition
        self.body = body
        self.orelse = orelse


class SwitchCase(AST):
    def __init__(
        self,
        body: Sequence[Statement],
        expression: Expression | None = None,
    ):
        super().__init__()
        self.body = body
        self.expression = expression


class Switch(AST):
    def __init__(
        self,
        cases: Sequence[SwitchCase],
        expression: Expression | None = None,
    ):
        super().__init__()
        self.cases = cases
        self.expression = expression


class Break(AST):
    pass


class Continue(AST):
    pass


class For(AST):
    def __init__(
        self,
        target: Identifier,
        initial_value: Expression,
        final_value: Expression,
        body: Sequence[Statement],
        increment_value: Expression | None = None,
    ):
        super().__init__()
        self.target = target
        self.initial_value = initial_value
        self.final_value = final_value
        self.body = body
        self.increment_value = increment_value


class ForIn(AST):
    def __init__(
        self,
        target: Identifier,
        iterate_value: Expression,
        body: Sequence[Statement],
    ):
        super().__init__()
        self.target = target
        self.iterate_value = iterate_value
        self.body = body


class While(AST):
    def __init__(
        self,
        condition: Expression,
        body: Sequence[Statement],
    ):
        super().__init__()
        self.condition = condition
        self.body = body


class Expr(AST):
    def __init__(self, value: Expression):
        super().__init__()
        self.value = value


Structure = Union[
    If,
    Switch,
    For,
    While,
]

Statement = Union[
    Assign,
    FunctionDef,
    Expr,
    Break,
    Continue,
]


class Ternary(AST):
    def __init__(
        self,
        condition: Expression,
        true_value: Expression,
        false_value: Expression,
    ):
        super().__init__()
        self.condition = condition
        self.true_value = true_value
        self.false_value = false_value


class And(AST):
    pass


class Or(AST):
    pass


BooleanOperator = Union[And, Or]


class Boolean(AST):
    def __init__(
        self,
        operator: BooleanOperator,
        values: Sequence[Expression],
    ):
        super().__init__()
        self.operator = operator
        self.values = values


class Binary(AST):
    def __init__(
        self,
        left: Expression,
        operator: BinaryOperator,
        right: Expression,
    ):
        super().__init__()
        self.left = left
        self.operator = operator
        self.right = right


class Not(AST):
    pass


class UAdd(AST):
    pass


class USub(AST):
    pass


UnaryOperator = Union[Not, UAdd, USub]


class Unary(AST):
    def __init__(
        self,
        operator: UnaryOperator,
        operand: Expression,
    ):
        super().__init__()
        self.operator = operator
        self.operand = operand


class Equal(AST):
    pass


class NotEqual(AST):
    pass


class LessThan(AST):
    pass


class LessThanEqual(AST):
    pass


class GreaterThan(AST):
    pass


class GreaterThanEqual(AST):
    pass


CompareOperator = Union[
    Equal,
    NotEqual,
    LessThan,
    LessThanEqual,
    GreaterThan,
    GreaterThanEqual,
]


class Compare(AST):
    def __init__(
        self,
        left: Expression,
        operators: Sequence[CompareOperator],
        comparators: Sequence[Expression],
    ):
        super().__init__()
        self.left = left
        self.operators = operators
        self.comparators = comparators


Expression = Union[
    Ternary,
    Boolean,
    Binary,
    Unary,
    Compare,
    Structure,
    Call,
]
