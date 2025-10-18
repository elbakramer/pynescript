# Copyright 2024 Yunseong Hwang
#
# Licensed under the GNU Lesser General Public License Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.gnu.org/licenses/lgpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

import json

from contextlib import contextmanager
from contextlib import nullcontext
from enum import IntEnum
from enum import auto
from typing import ClassVar

from pynescript.ast import node as ast
from pynescript.ast.visitor import NodeVisitor


class Precedence(IntEnum):
    TEST = auto()  # '?', ':'
    OR = auto()  # 'or'
    AND = auto()  # 'and'
    EQ = auto()  # '==', '!='
    INEQ = auto()  # '>', '<', '>=', '<='
    CMP = INEQ
    EXPR = auto()
    ARITH = auto()  # '+', '-'
    TERM = auto()  # '*', '/', '%'
    FACTOR = auto()  # unary '+', unary '-', 'not'
    NOT = FACTOR
    ATOM = auto()

    def next(self):  # noqa: A003
        try:
            return self.__class__(self + 1)
        except ValueError:
            return self


class NodeUnparser(NodeVisitor):
    # ruff: noqa: N802, ARG002

    def __init__(self):
        self._source = []
        self._precedences = {}
        self._indent = 0

    def interleave(self, inter, f, seq):
        seq = iter(seq)
        try:
            f(next(seq))
        except StopIteration:
            pass
        else:
            for x in seq:
                inter()
                f(x)

    def items_view(self, traverser, items, *, single: bool = False):
        if len(items) == 1:
            traverser(items[0])
            if single:
                self.write(",")
        else:
            self.interleave(lambda: self.write(", "), traverser, items)

    def maybe_newline(self):
        if self._source:
            self.write("\n")

    def fill(self, text=""):
        self.maybe_newline()
        self.write("    " * self._indent + text)

    def write(self, *text):
        self._source.extend(text)

    @contextmanager
    def buffered(self, buffer=None):
        if buffer is None:
            buffer = []
        original_source = self._source
        self._source = buffer
        yield buffer
        self._source = original_source

    @contextmanager
    def block(self, *, extra=None):
        if extra:
            self.write(extra)
        self._indent += 1
        yield
        self._indent -= 1

    @contextmanager
    def delimit(self, start, end):
        self.write(start)
        yield
        self.write(end)

    def delimit_if(self, start, end, condition):
        if condition:
            return self.delimit(start, end)
        else:
            return nullcontext()

    def require_parens(self, precedence, node):
        return self.delimit_if("(", ")", self.get_precedence(node) > precedence)

    def get_precedence(self, node):
        return self._precedences.get(node, Precedence.TEST)

    def set_precedence(self, precedence, *nodes):
        for node in nodes:
            self._precedences[node] = precedence

    def traverse(self, node):
        if isinstance(node, list):
            for item in node:
                self.traverse(item)
        else:
            super().visit(node)

    def visit(self, node):
        self._source = []
        self.traverse(node)
        return "".join(self._source)

    def visit_Script(self, node: ast.Script):
        if node.annotations:
            for annotation in node.annotations:
                self.fill(annotation)
        self.traverse(node.body)

    def visit_Expression(self, node: ast.Expression):
        self.traverse(node.body)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.fill()
        if node.annotations:
            for annotation in node.annotations:
                self.fill(annotation)
            self.fill()
        if node.export:
            self.write("export ")
        if node.method:
            self.write("method ")
        self.write(node.name)
        with self.delimit("(", ")"):
            if node.args:
                self.items_view(self.traverse, node.args)
        self.write(" => ")
        if len(node.body) == 1 and isinstance(node.body[0], ast.Expr):
            self.traverse(node.body[0].value)
        else:
            with self.block():
                self.traverse(node.body)

    def visit_TypeDef(self, node: ast.TypeDef):
        self.fill()
        if node.annotations:
            for annotation in node.annotations:
                self.fill(annotation)
            self.fill()
        if node.export:
            self.write("export ")
        self.write("type ")
        self.write(node.name)
        with self.block():
            self.traverse(node.body)

    def visit_EnumDef(self, node: ast.EnumDef):
        self.fill()
        if node.annotations:
            for annotation in node.annotations:
                self.fill(annotation)
            self.fill()
        if node.export:
            self.write("export ")
        self.write("enum ")
        self.write(node.name)
        with self.block():
            self.traverse(node.body)

    def visit_Assign(self, node: ast.Assign):
        self.fill()
        if node.annotations:
            for annotation in node.annotations:
                self.fill(annotation)
            self.fill()
        if node.mode:
            self.traverse(node.mode)
            self.write(" ")
        if node.type:
            self.traverse(node.type)
            self.write(" ")
        self.traverse(node.target)
        if node.value:
            self.write(" = ")
            self.traverse(node.value)

    def visit_ReAssign(self, node: ast.ReAssign):
        self.fill()
        self.traverse(node.target)
        self.write(" := ")
        self.traverse(node.value)

    def visit_AugAssign(self, node: ast.AugAssign):
        self.fill()
        self.traverse(node.target)
        self.write(" ")
        self.traverse(node.op)
        self.write("= ")
        self.traverse(node.value)

    def visit_ForTo(self, node: ast.ForTo):
        self.write("for ")
        self.traverse(node.target)
        self.write(" = ")
        self.traverse(node.start)
        self.write(" to ")
        self.traverse(node.end)
        if node.step:
            self.write(" by ")
            self.traverse(node.step)
        with self.block():
            self.traverse(node.body)

    def visit_ForIn(self, node: ast.ForIn):
        self.write("for ")
        self.traverse(node.target)
        self.write(" in ")
        self.traverse(node.iter)
        with self.block():
            self.traverse(node.body)

    def visit_While(self, node: ast.While):
        self.write("while ")
        self.traverse(node.test)
        with self.block():
            self.traverse(node.body)

    def visit_If(self, node: ast.If):
        self.write("if ")
        self.traverse(node.test)
        with self.block():
            self.traverse(node.body)
        while (
            node.orelse
            and len(node.orelse) == 1
            and isinstance(node.orelse[0], ast.Expr)
            and isinstance(node.orelse[0].value, ast.If)
        ):
            node = node.orelse[0].value
            self.fill("else if ")
            self.traverse(node.test)
            with self.block():
                self.traverse(node.body)
        if node.orelse:
            self.fill("else")
            with self.block():
                self.traverse(node.orelse)

    def visit_Switch(self, node: ast.Switch):
        self.write("switch")
        if node.subject:
            self.write(" ")
            self.traverse(node.subject)
        with self.block():
            self.traverse(node.cases)

    def visit_Import(self, node: ast.Import):
        self.fill()
        self.write("import ")
        self.write(node.namespace)
        self.write("/")
        self.write(node.name)
        self.write("/")
        self.write(str(node.version))
        if node.alias:
            self.write(" as ")
            self.write(node.alias)

    def visit_Expr(self, node: ast.Expr):
        self.fill()
        self.traverse(node.value)

    def visit_Break(self, node: ast.Break):
        self.fill("break")

    def visit_Continue(self, node: ast.Continue):
        self.fill("continue")

    boolops: ClassVar = {
        "And": "and",
        "Or": "or",
    }

    boolop_precedence: ClassVar = {
        "and": Precedence.AND,
        "or": Precedence.OR,
    }

    def visit_BoolOp(self, node: ast.BoolOp):
        operator = self.boolops[node.op.__class__.__name__]
        operator_precedence = self.boolop_precedence[operator]

        def increasing_level_traverse(node):
            nonlocal operator_precedence
            operator_precedence = operator_precedence.next()
            self.set_precedence(operator_precedence, node)
            self.traverse(node)

        with self.require_parens(operator_precedence, node):
            s = f" {operator} "
            self.interleave(lambda: self.write(s), increasing_level_traverse, node.values)

    binop: ClassVar = {
        "Add": "+",
        "Sub": "-",
        "Mult": "*",
        "Div": "/",
        "Mod": "%",
    }

    binop_precedence: ClassVar = {
        "+": Precedence.ARITH,
        "-": Precedence.ARITH,
        "*": Precedence.TERM,
        "/": Precedence.TERM,
        "%": Precedence.TERM,
    }

    def visit_BinOp(self, node: ast.BinOp):
        operator = self.binop[node.op.__class__.__name__]
        operator_precedence = self.binop_precedence[operator]
        with self.require_parens(operator_precedence, node):
            left_precedence = operator_precedence
            right_precedence = operator_precedence.next()
            self.set_precedence(left_precedence, node.left)
            self.traverse(node.left)
            self.write(f" {operator} ")
            self.set_precedence(right_precedence, node.right)
            self.traverse(node.right)

    unop: ClassVar = {
        "Not": "not",
        "UAdd": "+",
        "USub": "-",
    }

    unop_precedence: ClassVar = {
        "not": Precedence.NOT,
        "+": Precedence.FACTOR,
        "-": Precedence.FACTOR,
    }

    def visit_UnaryOp(self, node: ast.UnaryOp):
        operator = self.unop[node.op.__class__.__name__]
        operator_precedence = self.unop_precedence[operator]
        with self.require_parens(operator_precedence, node):
            self.write(operator)
            if isinstance(node.op, ast.Not):
                self.write(" ")
            self.set_precedence(operator_precedence, node.operand)
            self.traverse(node.operand)

    def visit_Conditional(self, node: ast.Conditional):
        with self.require_parens(Precedence.TEST, node):
            self.set_precedence(Precedence.TEST.next(), node.test, node.body)
            self.traverse(node.test)
            self.write(" ? ")
            self.traverse(node.body)
            self.write(" : ")
            self.set_precedence(Precedence.TEST, node.orelse)
            self.traverse(node.orelse)

    cmpops: ClassVar = {
        "Eq": "==",
        "NotEq": "!=",
        "Lt": "<",
        "LtE": "<=",
        "Gt": ">",
        "GtE": ">=",
    }

    cmpop_precedence: ClassVar = {
        "==": Precedence.EQ,
        "!=": Precedence.EQ,
        "<": Precedence.INEQ,
        "<=": Precedence.INEQ,
        ">": Precedence.INEQ,
        ">=": Precedence.INEQ,
    }

    def visit_Compare(self, node: ast.Compare):
        with self.require_parens(Precedence.CMP, node):
            self.set_precedence(Precedence.CMP.next(), node.left, *node.comparators)
            self.traverse(node.left)
            for o, e in zip(node.ops, node.comparators, strict=True):
                operator = self.cmpops[o.__class__.__name__]
                self.write(f" {operator} ")
                self.traverse(e)

    def visit_Call(self, node: ast.Call):
        self.set_precedence(Precedence.ATOM, node.func)
        self.traverse(node.func)
        with self.delimit("(", ")"):
            if node.args:
                self.items_view(self.traverse, node.args)

    def visit_Constant(self, node: ast.Constant):
        if node.kind:
            self.write(node.value)
        elif isinstance(node.value, bool):
            if node.value:
                self.write("true")
            else:
                self.write("false")
        elif isinstance(node.value, str):
            if '"' in node.value and "'" not in node.value:
                self.write(repr(node.value))
            else:
                self.write(json.dumps(node.value, ensure_ascii=False))
        else:
            self.write(repr(node.value))

    def visit_Attribute(self, node: ast.Attribute):
        self.set_precedence(Precedence.ATOM, node.value)
        self.traverse(node.value)
        self.write(".")
        self.write(node.attr)

    def visit_Subscript(self, node: ast.Subscript):
        self.traverse(node.value)
        with self.delimit("[", "]"):
            if node.slice:
                if isinstance(node.slice, ast.Tuple):
                    self.items_view(self.traverse, node.slice.elts)
                else:
                    self.traverse(node.slice)

    def visit_Name(self, node: ast.Name):
        self.write(node.id)

    def visit_Tuple(self, node: ast.Tuple):
        with self.delimit("[", "]"):
            if node.elts:
                self.items_view(self.traverse, node.elts)

    def visit_Qualify(self, node: ast.Qualify):
        self.traverse(node.qualifier)
        self.write(" ")
        self.traverse(node.value)

    def visit_Specialize(self, node: ast.Specialize):
        self.traverse(node.value)
        with self.delimit("<", ">"):
            if node.args:
                if isinstance(node.args, ast.Tuple):
                    self.items_view(self.traverse, node.args.elts)
                else:
                    self.traverse(node.args)

    def visit_Var(self, node: ast.Var):
        self.write("var")

    def visit_VarIp(self, node: ast.VarIp):
        self.write("varip")

    def visit_Const(self, node: ast.Const):
        self.write("const")

    def visit_Input(self, node: ast.Input):
        self.write("input")

    def visit_Sipmle(self, node: ast.Simple):
        self.write("simple")

    def visit_Series(self, node: ast.Series):
        self.write("series")

    def visit_And(self, node: ast.And):
        self.write("and")

    def visit_Or(self, node: ast.Or):
        self.write("or")

    def visit_Add(self, node: ast.Add):
        self.write("+")

    def visit_Sub(self, node: ast.Sub):
        self.write("-")

    def visit_Mult(self, node: ast.Mult):
        self.write("*")

    def visit_Div(self, node: ast.Div):
        self.write("/")

    def visit_Mod(self, node: ast.Mod):
        self.write("%")

    def visit_Not(self, node: ast.Not):
        self.write("not")

    def visit_UAdd(self, node: ast.UAdd):
        self.write("+")

    def visit_USub(self, node: ast.USub):
        self.write("-")

    def visit_Eq(self, node: ast.Eq):
        self.write("==")

    def visit_NotEq(self, node: ast.NotEq):
        self.write("!=")

    def visit_Lt(self, node: ast.Lt):
        self.write("<")

    def visit_LtE(self, node: ast.LtE):
        self.write("<=")

    def visit_Gt(self, node: ast.Gt):
        self.write(">")

    def visit_GtE(self, node: ast.GtE):
        self.write(">=")

    def visit_Param(self, node: ast.Param):
        if node.type:
            self.traverse(node.type)
            self.write(" ")
        self.write(node.name)
        if node.default:
            self.write("=")
            self.traverse(node.default)

    def visit_Arg(self, node: ast.Arg):
        if node.name:
            self.write(node.name)
            self.write("=")
        self.traverse(node.value)

    def visit_Case(self, node: ast.Case):
        self.fill()
        if node.pattern:
            self.traverse(node.pattern)
            self.write(" ")
        self.write("=> ")
        if len(node.body) == 1 and isinstance(node.body[0], ast.Expr):
            self.traverse(node.body[0].value)
        else:
            with self.block():
                self.traverse(node.body)

    def visit_Comment(self, node: ast.Comment):
        self.fill(node.value)
