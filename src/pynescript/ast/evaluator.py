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

import itertools
import math
import operator
import statistics

from typing import Any

from pynescript.ast import node as ast
from pynescript.ast.visitor import NodeVisitor


class NodeLiteralEvaluator(NodeVisitor):
    # ruff: noqa: N802

    def __init__(self, context: dict[str, Any] | None = None):
        self.context = context or {}
        self.context.update(
            {
                "math.pi": math.pi,
                "math.e": math.e,
                "math.phi": (1 + math.sqrt(5)) / 2,
                "math.rphi": 2 / (1 + math.sqrt(5)),
            }
        )

    def visit_Script(self, node: ast.Script):
        for stmt in node.body:
            self.visit(stmt)

    def visit_Assign(self, node: ast.Assign):
        if node.value:
            value = self.visit(node.value)
            if isinstance(node.target, ast.Name):
                self.context[node.target.id] = value
            else:
                self._error(f"Unsupported assignment target: {type(node.target)}")

    def visit_BoolOp(self, node: ast.BoolOp):
        if isinstance(node.op, ast.And):
            return all(self.visit(value) for value in node.values)
        if isinstance(node.op, ast.Or):
            return any(self.visit(value) for value in node.values)
        msg = f"unexpected node operator: {node.op}"
        raise ValueError(msg)

    def visit_BinOp(self, node: ast.BinOp):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return operator.add(left, right)
        elif isinstance(node.op, ast.Sub):
            return operator.sub(left, right)
        elif isinstance(node.op, ast.Mult):
            return operator.mul(left, right)
        elif isinstance(node.op, ast.Div):
            return operator.truediv(left, right)
        elif isinstance(node.op, ast.Mod):
            return operator.mod(left, right)
        else:
            msg = f"Unsupported binary operator: {type(node.op)}"
            raise NotImplementedError(msg)

    def visit_UnaryOp(self, node: ast.UnaryOp):
        if isinstance(node.op, ast.Not):
            return operator.not_(self.visit(node.operand))
        if isinstance(node.op, ast.UAdd):
            return operator.pos(self.visit(node.operand))
        if isinstance(node.op, ast.USub):
            return operator.neg(self.visit(node.operand))
        msg = f"unexpected node operator: {node.op}"
        raise ValueError(msg)

    def visit_Conditional(self, node: ast.Conditional) -> Any:
        test_result = self.visit(node.test)
        if test_result:
            return self.visit(node.body)
        else:
            return self.visit(node.orelse)

    def visit_Compare(self, node: ast.Compare) -> Any:
        comparator_list = [node.left, *node.comparators]
        comparators = map(self.visit, comparator_list)
        compare_ops = [self.visit(op) for op in node.ops]
        comparator_pairs = list(itertools.pairwise(comparators))
        pairs = zip(compare_ops, comparator_pairs, strict=True)
        for op, (left, right) in pairs:
            if not op(left, right):
                return False
        return True

    def visit_Eq(self, _node: ast.Eq):
        return operator.eq

    def visit_NotEq(self, _node: ast.NotEq):
        return operator.ne

    def visit_Lt(self, _node: ast.Lt):
        return operator.lt

    def visit_LtE(self, _node: ast.LtE):
        return operator.le

    def visit_Gt(self, _node: ast.Gt):
        return operator.gt

    def visit_GtE(self, _node: ast.GtE):
        return operator.ge

    def visit_Constant(self, node: ast.Constant):
        if node.kind:
            msg = f"unexpected constant kind: {node.kind!s}"
            raise ValueError(msg)
        return node.value

    def visit_Tuple(self, node: ast.Tuple) -> Any:
        return [self.visit(elt) for elt in node.elts]

    def visit_Call(self, node: ast.Call):
        func = self.visit(node.func)
        args = []

        kwargs = {}

        for arg in node.args:
            if arg.name:
                kwargs[arg.name] = self.visit(arg.value)

            else:
                args.append(self.visit(arg.value))

        # Handle built-in functions
        if isinstance(func, str):
            return self._call_builtin(func, args)
        else:
            # For now, assume func is callable
            return func(*args, **kwargs)

    def visit_EnumDef(self, node: ast.EnumDef):
        enum_name = node.name
        enum_members = {}
        for stmt in node.body:
            member_name = None
            if isinstance(stmt, ast.Assign) and isinstance(stmt.target, ast.Name):
                member_name = stmt.target.id
            elif isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Name):
                member_name = stmt.value.id
            else:
                self._error(f"Unsupported statement in enum body: {type(stmt)}")

            if member_name:
                # The value is symbolic, representing member access
                enum_members[member_name] = f"{enum_name}.{member_name}"

        # Store the enum definition in the context
        self.context[enum_name] = enum_members
    def _build_builtin_map(self):
        # Argument count constants
        unary = 1
        binary = 2
        ternary = 3
        quaternary = 4
        quinary = 5

        builtins = {
            "abs": (
                lambda args: abs(args[0])
                if len(args) == unary
                else self._error("abs takes exactly one argument")
            ),
            "math.max": lambda args: max(args),
            "math.min": lambda args: min(args),
            "math.abs": (
                lambda args: abs(args[0])
                if len(args) == unary
                else self._error("math.abs takes exactly one argument")
            ),
            "math.sqrt": (
                lambda args: math.sqrt(args[0])
                if len(args) == unary
                else self._error("math.sqrt takes exactly one argument")
            ),
            "math.round": (
                lambda args: (
                    round(args[0])
                    if len(args) == unary
                    else round(args[0], args[1])
                    if len(args) == binary
                    else self._error("math.round takes one or two arguments")
                )
            ),
            "math.floor": (
                lambda args: math.floor(args[0])
                if len(args) == unary
                else self._error("math.floor takes exactly one argument")
            ),
            "math.ceil": (
                lambda args: math.ceil(args[0])
                if len(args) == unary
                else self._error("math.ceil takes exactly one argument")
            ),
            "math.pow": (
                lambda args: math.pow(args[0], args[1])
                if len(args) == binary
                else self._error("math.pow takes exactly two arguments")
            ),
            "math.log": (
                lambda args: (
                    math.log(args[0])
                    if len(args) == unary
                    else math.log(args[0], args[1])
                    if len(args) == binary
                    else self._error("math.log takes one or two arguments")
                )
            ),
            "math.sin": (
                lambda args: math.sin(args[0])
                if len(args) == unary
                else self._error("math.sin takes exactly one argument")
            ),
            "math.cos": (
                lambda args: math.cos(args[0])
                if len(args) == unary
                else self._error("math.cos takes exactly one argument")
            ),
            "math.tan": (
                lambda args: math.tan(args[0])
                if len(args) == unary
                else self._error("math.tan takes exactly one argument")
            ),
            "math.acos": (
                lambda args: math.acos(args[0])
                if len(args) == unary
                else self._error("math.acos takes exactly one argument")
            ),
            "math.asin": (
                lambda args: math.asin(args[0])
                if len(args) == unary
                else self._error("math.asin takes exactly one argument")
            ),
            "math.atan": (
                lambda args: math.atan(args[0])
                if len(args) == unary
                else self._error("math.atan takes exactly one argument")
            ),
            "math.exp": (
                lambda args: math.exp(args[0])
                if len(args) == unary
                else self._error("math.exp takes exactly one argument")
            ),
            "math.log10": (
                lambda args: math.log10(args[0])
                if len(args) == unary
                else self._error("math.log10 takes exactly one argument")
            ),
            "math.sign": (
                lambda args: (1 if args[0] > 0 else -1 if args[0] < 0 else 0)
                if len(args) == unary
                else self._error("math.sign takes exactly one argument")
            ),
            "math.sum": (
                lambda args: sum(args[0])
                if len(args) == unary and isinstance(args[0], list)
                else self._error("math.sum takes an array argument")
            ),
            "math.avg": (
                lambda args: statistics.mean(args[0])
                if len(args) == unary and isinstance(args[0], list) and args[0]
                else self._error("math.avg takes a non-empty array")
            ),
            "math.todegrees": (
                lambda args: math.degrees(args[0])
                if len(args) == unary
                else self._error("math.todegrees takes one argument")
            ),
            "math.toradians": (
                lambda args: math.radians(args[0])
                if len(args) == unary
                else self._error("math.toradians takes one argument")
            ),
            "str.length": (
                lambda args: len(args[0])
                if len(args) == unary and isinstance(args[0], str)
                else self._error("str.length takes a string argument")
            ),
            "str.upper": (
                lambda args: args[0].upper()
                if len(args) == unary and isinstance(args[0], str)
                else self._error("str.upper takes a string argument")
            ),
            "str.lower": (
                lambda args: args[0].lower()
                if len(args) == unary and isinstance(args[0], str)
                else self._error("str.lower takes a string argument")
            ),
            "str.contains": (
                lambda args: args[1] in args[0]
                if (
                    len(args) == binary
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                )
                else self._error("str.contains takes two string arguments")
            ),
            "str.startswith": (
                lambda args: args[0].startswith(args[1])
                if (
                    len(args) == binary
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                )
                else self._error("str.startswith takes two string arguments")
            ),
            "str.substring": (
                lambda args: (
                    args[0][args[1]:]
                    if (
                        len(args) == binary
                        and isinstance(args[0], str)
                        and isinstance(args[1], int)
                    )
                    else args[0][args[1]:args[2]]
                    if (
                        len(args) == ternary
                        and isinstance(args[0], str)
                        and isinstance(args[1], int)
                        and isinstance(args[2], int)
                    )
                    else self._error("str.substring takes string and 1-2 ints")
                )
            ),
            "str.endswith": (
                lambda args: args[0].endswith(args[1])
                if (
                    len(args) == binary
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                )
                else self._error("str.endswith takes two string arguments")
            ),
            "str.repeat": (
                lambda args: args[0] * args[1]
                if (
                    len(args) == binary
                    and isinstance(args[0], str)
                    and isinstance(args[1], int)
                )
                else self._error("str.repeat takes string and int")
            ),
            "str.replace": (
                lambda args: args[0].replace(args[1], args[2], 1)
                if (
                    len(args) == ternary
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                    and isinstance(args[2], str)
                )
                else self._error("str.replace takes three string arguments")
            ),
            "str.replace_all": (
                lambda args: args[0].replace(args[1], args[2])
                if (
                    len(args) == ternary
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                    and isinstance(args[2], str)
                )
                else self._error("str.replace_all takes three strings")
            ),
            "str.split": (
                lambda args: (
                    args[0].split(args[1])
                    if (
                        len(args) == binary
                        and isinstance(args[0], str)
                        and isinstance(args[1], str)
                    )
                    else args[0].split()
                    if len(args) == unary and isinstance(args[0], str)
                    else self._error("str.split takes str and opt separator")
                )
            ),
            "str.trim": (
                lambda args: args[0].strip()
                if len(args) == unary and isinstance(args[0], str)
                else self._error("str.trim takes a string argument")
            ),
            "str.tonumber": (
                lambda args: float(args[0])
                if len(args) == unary and isinstance(args[0], str)
                else self._error("str.tonumber takes a string argument")
            ),
            "str.tostring": (
                lambda args: str(args[0])
                if len(args) == unary
                else self._error("str.tostring takes one argument")
            ),
            "array.size": (
                lambda args: len(args[0])
                if len(args) == unary and isinstance(args[0], list)
                else self._error("array.size takes an array argument")
            ),
            "array.get": (
                lambda args: args[0][args[1]]
                if (
                    len(args) == binary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("array.get takes array and index")
            ),
            "array.push": (
                lambda args: args[0] + [args[1]]
                if len(args) == binary and isinstance(args[0], list)
                else self._error("array.push takes array and value")
            ),
            "array.pop": (
                lambda args: args[0][:-1]
                if len(args) == unary and isinstance(args[0], list)
                else self._error("array.pop takes one array argument")
            ),
            "array.slice": (
                lambda args: args[0][args[1]:args[2]]
                if (
                    len(args) == ternary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and isinstance(args[2], int)
                )
                else self._error("array.slice takes array, start, end")
            ),
            "array.abs": (
                lambda args: [abs(x) for x in args[0]]
                if len(args) == unary and isinstance(args[0], list)
                else self._error("array.abs takes an array argument")
            ),
            "array.avg": (
                lambda args: statistics.mean(args[0])
                if len(args) == unary and isinstance(args[0], list) and args[0]
                else self._error("array.avg takes a non-empty array")
            ),
            "array.clear": (
                lambda args: []
                if len(args) == unary and isinstance(args[0], list)
                else self._error("array.clear takes an array argument")
            ),
            "array.concat": (
                lambda args: args[0] + args[1]
                if len(args) == binary
                and isinstance(args[0], list)
                and isinstance(args[1], list)
                else self._error("array.concat takes two array arguments")
            ),
            "array.copy": (
                lambda args: args[0].copy()
                if len(args) == unary and isinstance(args[0], list)
                else self._error("array.copy takes an array argument")
            ),
            "array.covariance": (
                lambda args: self._covariance(args[0], args[1], args[2])
                if (
                    len(args) == ternary
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], int)
                )
                else self._error("array.covariance takes two series and length")
            ),
            "array.every": (
                lambda args: all(args[1](x) for x in args[0])
                if (
                    len(args) == binary
                    and isinstance(args[0], list)
                    and callable(args[1])
                )
                else self._error("array.every takes array and predicate")
            ),
            "array.fill": (
                lambda args: [args[1]] * len(args[0])
                if len(args) == binary and isinstance(args[0], list)
                else self._error("array.fill takes array and fill value")
            ),
            "array.first": (
                lambda args: args[0][0]
                if len(args) == unary and isinstance(args[0], list) and args[0]
                else self._error("array.first takes non-empty array")
            ),
            "array.from": (
                lambda args: list(args)
                if len(args) > 0
                else self._error("array.from takes at least one argument")
            ),
            "array.includes": (
                lambda args: args[1] in args[0]
                if len(args) == binary and isinstance(args[0], list)
                else self._error("array.includes takes array and search value")
            ),
            "array.indexof": (
                lambda args: args[0].index(args[1])
                if args[1] in args[0]
                else -1
                if len(args) == binary and isinstance(args[0], list)
                else self._error("array.indexof takes array and search value")
            ),
            "array.insert": (
                lambda args: [*args[0][:args[1]], args[2], *args[0][args[1]:]]
                if (
                    len(args) == ternary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("array.insert takes array, index, and value")
            ),
            "array.join": (
                lambda args: args[1].join(str(x) for x in args[0])
                if len(args) == binary
                and isinstance(args[0], list)
                and isinstance(args[1], str)
                else self._error("array.join takes array and separator string")
            ),
            "array.last": (
                lambda args: args[0][-1]
                if len(args) == unary and isinstance(args[0], list) and args[0]
                else self._error("array.last takes non-empty array")
            ),
            "array.lastindexof": (
                lambda args: len(args[0]) - 1 - args[0][::-1].index(args[1])
                if args[1] in args[0]
                else -1
                if len(args) == binary and isinstance(args[0], list)
                else self._error("array.lastindexof takes array and value")
            ),
            "array.max": (
                lambda args: max(args[0])
                if len(args) == unary and isinstance(args[0], list) and args[0]
                else self._error("array.max takes non-empty array")
            ),
            "array.median": (
                lambda args: statistics.median(args[0])
                if len(args) == unary and isinstance(args[0], list) and args[0]
                else self._error("array.median takes non-empty array")
            ),
            "array.min": (
                lambda args: min(args[0])
                if len(args) == unary and isinstance(args[0], list) and args[0]
                else self._error("array.min takes non-empty array")
            ),
            "array.range": (
                lambda args: list(range(args[0], args[1] + 1))
                if len(args) == binary
                and isinstance(args[0], int)
                and isinstance(args[1], int)
                else self._error("array.range takes start and end integers")
            ),
            "array.remove": (
                lambda args: args[0][:args[1]] + args[0][args[1] + 1:]
                if (
                    len(args) == binary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and 0 <= args[1] < len(args[0])
                )
                else self._error("array.remove takes array and valid index")
            ),
            "array.reverse": (
                lambda args: args[0][::-1]
                if len(args) == unary and isinstance(args[0], list)
                else self._error("array.reverse takes an array argument")
            ),
            "array.set": (
                lambda args: (
                    [*args[0][:args[1]], args[2], *args[0][args[1] + 1:]]
                )
                if (
                    len(args) == ternary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and 0 <= args[1] < len(args[0])
                )
                else self._error("array.set takes array, index, and value")
            ),
            "array.shift": (
                lambda args: args[0][1:]
                if len(args) == unary and isinstance(args[0], list) and args[0]
                else self._error("array.shift takes non-empty array")
            ),
            "array.some": (
                lambda args: any(args[1](x) for x in args[0])
                if (
                    len(args) == binary
                    and isinstance(args[0], list)
                    and callable(args[1])
                )
                else self._error("array.some takes array and predicate")
            ),
            "array.sort": (
                lambda args: sorted(args[0])
                if len(args) == unary and isinstance(args[0], list)
                else self._error("array.sort takes an array argument")
            ),
            "array.sum": (
                lambda args: sum(args[0])
                if len(args) == unary and isinstance(args[0], list)
                else self._error("array.sum takes an array argument")
            ),
            "array.unshift": (
                lambda args: [args[1]] + args[0]
                if len(args) == binary and isinstance(args[0], list)
                else self._error("array.unshift takes array and value")
            ),
            "color.new": (
                lambda args: f"color({args[0]})"
                if len(args) == unary
                else self._error("color.new takes one argument")
            ),
            "ta.sma": (
                lambda args: (
                    [
                        None if i < args[1] - 1 else statistics.mean(args[0][i - args[1] + 1 : i + 1])
                        for i in range(len(args[0]))
                    ]
                    if (
                        len(args) == binary
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                    )
                    else self._error("ta.sma takes series and period")
                )
            ),
            "ta.ema": (
                lambda args: self._ema(args[0], args[1])
                if (
                    len(args) == binary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.ema takes series and period")
            ),
            "ta.rsi": (
                lambda args: self._rsi(args[0], args[1])
                if (
                    len(args) == binary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.rsi takes series and period")
            ),
            "ta.stdev": (
                lambda args: (
                    statistics.stdev(args[0][-args[1]:])
                    if (
                        len(args) == binary
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                        and len(args[0][-args[1]:]) > 1
                    )
                    else self._error("ta.stdev takes series and period")
                )
            ),
            "ta.change": (
                lambda args: (
                    args[0][-1] - args[0][-args[1] - 1]
                    if (
                        len(args) == binary
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                        and len(args[0]) > args[1]
                    )
                    else self._error("ta.change takes series and period")
                )
            ),
            "ta.highest": (
                lambda args: (
                    max(args[0][-args[1]:])
                    if (
                        len(args) == binary
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                    )
                    else self._error("ta.highest takes series and period")
                )
            ),
            "ta.lowest": (
                lambda args: (
                    min(args[0][-args[1]:])
                    if (
                        len(args) == binary
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                    )
                    else self._error("ta.lowest takes series and period")
                )
            ),
            "ta.range": (
                lambda args: (
                    max(args[0][-args[1]:]) - min(args[0][-args[1]:])
                    if (
                        len(args) == binary
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                    )
                    else self._error("ta.range takes series and period")
                )
            ),
            "ta.wma": (
                lambda args: self._wma(args[0], args[1])
                if (
                    len(args) == binary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.wma takes series and period")
            ),
            "ta.bb": (
                lambda args: self._bollinger_bands(args[0], args[1], args[2])
                if (
                    len(args) == ternary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and isinstance(args[2], (int, float))
                )
                else self._error("ta.bb takes series, period, and multiplier")
            ),
            "ta.macd": (
                lambda args: self._macd(args[0], args[1], args[2], args[3])
                if (
                    len(args) == quaternary
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and isinstance(args[2], int)
                    and isinstance(args[3], int)
                )
                else self._error("ta.macd takes series, fast, slow, signal")
            ),
            "ta.atr": (
                lambda args: self._atr(
                    args[0],
                    args[1],
                    args[2],
                    args[3],
                )
                if (
                    len(args) == quaternary
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], int)
                )
                else self._error("ta.atr takes highs, lows, closes, period")
            ),
            "ta.crossover": (
                lambda args: (
                    args[0][-1] > args[1][-1] and args[0][-2] <= args[1][-2]
                    if (
                        len(args) == binary
                        and isinstance(args[0], list)
                        and isinstance(args[1], (list, int, float))
                        and len(args[0]) >= binary
                    )
                    else self._error("ta.crossover takes two series")
                )
            ),
            "ta.crossunder": (
                lambda args: (
                    args[0][-1] < args[1][-1] and args[0][-2] >= args[1][-2]
                    if (
                        len(args) == binary
                        and isinstance(args[0], list)
                        and isinstance(args[1], (list, int, float))
                        and len(args[0]) >= binary
                    )
                    else self._error("ta.crossunder takes two series")
                )
            ),
            "ta.cross": (
                lambda args: self._cross(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], (list, int, float))
                )
                else self._error("ta.cross takes two series")
            ),
            "ta.falling": (
                lambda args: self._falling(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.falling takes series and length")
            ),
            "ta.highestbars": (
                lambda args: self._highestbars(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.highestbars takes series and period")
            ),
            "ta.lowestbars": (
                lambda args: self._lowestbars(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.lowestbars takes series and period")
            ),
            "ta.rising": (
                lambda args: self._rising(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.rising takes series and length")
            ),
            "ta.rma": (
                lambda args: self._rma(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.rma takes series and period")
            ),
            "ta.vwap": (
                lambda args: self._vwap(args[0], args[1], args[2], args[3])
                if (
                    len(args) == 4
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], list)
                )
                else self._error("ta.vwap takes highs, lows, closes, volumes")
            ),
            "ta.vwma": (
                lambda args: self._vwma(args[0], args[1], args[2])
                if (
                    len(args) == 3
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], int)
                )
                else self._error("ta.vwma takes series, volumes, period")
            ),
            "ta.hma": (
                lambda args: self._hma(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.hma takes series and period")
            ),
            "ta.sar": (
                lambda args: self._sar(
                    args[0],
                    args[1],
                    args[2],
                    args[3],
                    args[4],
                    args[5],
                )
                if (
                    len(args) == 6
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], (int, float))
                    and isinstance(args[4], (int, float))
                    and isinstance(args[5], (int, float))
                )
                else self._error("ta.sar takes highs, lows, closes, accel, max_accel, increment")
            ),
            "ta.tsi": (
                lambda args: self._tsi(args[0], args[1], args[2])
                if (
                    len(args) == 3
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and isinstance(args[2], int)
                )
                else self._error("ta.tsi takes series, long_period, short_period")
            ),
        }
        return builtins

    def _call_builtin(self, name: str, args):
        dispatch = getattr(self, "_builtin_dispatch", None)
        if dispatch is None:
            dispatch = self._build_builtin_map()
            self._builtin_dispatch = dispatch
        handler = dispatch.get(name)
        if handler is None:
            msg = f"Unknown built-in function: {name}"
            raise ValueError(msg)
        return handler(args)

    def _error(self, msg: str):
        raise ValueError(msg)

    def _covariance(self, series1, series2, length):
        if len(series1) < length or len(series2) < length:
            self._error("Series length must be greater than or equal to the lookback period.")
        series1_segment = series1[-length:]
        series2_segment = series2[-length:]
        mean1 = statistics.mean(series1_segment)
        mean2 = statistics.mean(series2_segment)
        covariance = (
            sum(
                (x - mean1) * (y - mean2)
                for x, y in zip(series1_segment, series2_segment, strict=True)
            )
            / (length - 1)
        )
        return covariance

    def _ema(self, series, period):
        res = []
        if not series:
            return res
        multiplier = 2 / (period + 1)
        # The first EMA is just the first price
        res.append(series[0])
        for i in range(1, len(series)):
            ema = (series[i] - res[-1]) * multiplier + res[-1]
            res.append(ema)
        return res

    def _rsi(self, series, period):
        if len(series) < period:
            return None
        changes = [series[i] - series[i - 1] for i in range(1, len(series))]
        gains = [max(c, 0) for c in changes[-period:]]
        losses = [abs(min(c, 0)) for c in changes[-period:]]
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        if avg_loss == 0:
            return 100.0
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def _macd(self, series: list, fast: int, slow: int, signal: int):
        if len(series) < slow:
            return [0.0, 0.0, 0.0]
        fast_ema = self._ema(series, fast)
        slow_ema = self._ema(series, slow)
        macd = fast_ema - slow_ema
        # Note: This is a simplified MACD, a real one needs historical EMA values
        signal_line = self._ema(
            [macd],
            signal,
        )
        histogram = macd - signal_line
        return macd, signal_line, histogram

    def _atr(
        self,
        highs: list,
        lows: list,
        closes: list,
        period: int,
    ) -> float:
        min_len = 2
        if len(highs) < min_len or len(lows) < min_len or len(closes) < min_len:
            return 0.0
        tr_values = []
        for i in range(1, len(highs)):
            high = highs[i]
            low = lows[i]
            prev_close = closes[i - 1]

            tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
            tr_values.append(tr)
        if len(tr_values) < period:
            return statistics.mean(tr_values) if tr_values else 0.0
        return self._ema(tr_values, period)

    def _stoch(
        self,
        highs: list,
        lows: list,
        closes: list,
        k_period: int,
        d_period: int,
    ):
        if (
            len(highs) < k_period
            or len(lows) < k_period
            or len(closes) < k_period
        ):
            return 0.0, 0.0

        k_values = []
        for i in range(k_period - 1, len(closes)):
            high_win = highs[i - k_period + 1:i + 1]
            low_win = lows[i - k_period + 1:i + 1]
            close = closes[i]
            lowest_low = min(low_win)
            highest_high = max(high_win)
            if highest_high == lowest_low:
                k = 100.0
            else:
                k = 100 * (close - lowest_low) / (highest_high - lowest_low)
            k_values.append(k)

        if len(k_values) < d_period:
            return k_values[-1], 0.0

        d_values = self._ema(k_values, d_period)
        return k_values[-1], d_values

    def _adx(
        self,
        highs: list,
        lows: list,
        closes: list,
        period: int,
    ) -> float:
        min_len = period + 1
        if (
            len(highs) < min_len
            or len(lows) < min_len
            or len(closes) < min_len
        ):
            return 0.0

        true_ranges = []
        plus_dms = []
        minus_dms = []

        for i in range(1, len(highs)):
            high = highs[i]
            low = lows[i]
            prev_close = closes[i - 1]

            tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
            true_ranges.append(tr)

            high_diff = high - highs[i - 1]
            low_diff = lows[i - 1] - low

            plus_dm = (
                high_diff if high_diff > low_diff and high_diff > 0 else 0.0
            )
            minus_dm = (
                low_diff if low_diff > high_diff and low_diff > 0 else 0.0
            )
            plus_dms.append(plus_dm)
            minus_dms.append(minus_dm)

        if not true_ranges:
            return 0.0

        atr = self._ema(true_ranges, period)
        if atr == 0:
            return 0.0

        plus_di = 100 * self._ema(plus_dms, period) / atr
        minus_di = 100 * self._ema(minus_dms, period) / atr

        if plus_di + minus_di == 0:
            return 0.0

        dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
        return self._ema([dx], period)

    def _cci(
        self,
        highs: list,
        lows: list,
        closes: list,
        period: int,
    ) -> float:
        if len(highs) < period or len(lows) < period or len(closes) < period:
            return 0.0

        # Calculate Typical Price for each period
        typical_prices = [
            (highs[i] + lows[i] + closes[i]) / 3
            for i in range(len(closes))
        ]

        # Calculate the Simple Moving Average of the Typical Price
        sma_tp = statistics.mean(typical_prices[-period:])

        # Calculate the Mean Deviation
        mean_dev = statistics.mean(
            [abs(tp - sma_tp) for tp in typical_prices[-period:]]
        )

        if mean_dev == 0:
            return 0.0

        cci = (typical_prices[-1] - sma_tp) / (0.015 * mean_dev)
        return cci

    def _roc(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        return ((series[-1] - series[-period]) / series[-period]) * 100.0

    def _wpr(
        self,
        highs: list,
        lows: list,
        closes: list,
        period: int,
    ) -> float:
        if len(highs) < period or len(lows) < period or len(closes) < period:
            return 0.0

        highest_high = max(highs[-period:])
        lowest_low = min(lows[-period:])
        current_close = closes[-1]

        if highest_high == lowest_low:
            return 0.0

        wpr = (
            (highest_high - current_close) / (highest_high - lowest_low)
        ) * -100.0
        return wpr

    def _obv(self, closes: list, volumes: list) -> int:
        min_len = 2
        if len(closes) != len(volumes) or len(closes) < min_len:
            return 0

        obv = 0
        for i in range(1, len(closes)):
            if closes[i] > closes[i - 1]:
                obv += volumes[i]
            elif closes[i] < closes[i - 1]:
                obv -= volumes[i]
        return obv

    def _mfi(
        self,
        highs: list,
        lows: list,
        closes: list,
        volumes: list,
        period: int,
    ) -> float:
        if (
            len(highs) < period
            or len(lows) < period
            or len(closes) < period
            or len(volumes) < period
        ):
            return 50.0

        typical_prices = [
            (highs[i] + lows[i] + closes[i]) / 3
            for i in range(len(closes))
        ]

        money_flows = [
            typical_prices[i] * volumes[i] for i in range(len(typical_prices))
        ]

        positive_mf = []
        negative_mf = []

        for i in range(1, len(typical_prices)):
            if typical_prices[i] > typical_prices[i - 1]:
                positive_mf.append(money_flows[i])
                negative_mf.append(0)
            else:
                negative_mf.append(money_flows[i])
                positive_mf.append(0)

        sum_pos_mf = sum(positive_mf[-period:])
        sum_neg_mf = sum(negative_mf[-period:])

        if sum_neg_mf == 0:
            return 100.0

        money_ratio = sum_pos_mf / sum_neg_mf
        mfi = 100 - (100 / (1 + money_ratio))
        return mfi

    def _cum(self, series: list) -> float:
        return sum(series)

    def _dev(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        sma = statistics.mean(series[-period:])
        return series[-1] - sma

    def _max(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        return max(series[-period:])

    def _min(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        return min(series[-period:])

    def _mom(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        return series[-1] - series[-period]

    def _median(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        return statistics.median(series[-period:])

    def _mode(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        return statistics.mode(series[-period:])

    def _percentrank(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        window = series[-period:]
        value = series[-1]
        return (
            sum(1 for x in window if x < value) / (len(window) - 1)
        ) * 100

    def _variance(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        return statistics.variance(series[-period:])

    def _valuewhen(
        self,
        condition: list,
        source: list,
        occurrence: int,
    ) -> Any:
        if len(condition) != len(source):
            self._error("condition and source must have same length")
        indices = [i for i, x in enumerate(condition) if x]
        if len(indices) > occurrence:
            return source[indices[-(occurrence + 1)]]
        return None

    def generic_visit(self, node: ast.AST):
        msg = f"unexpected type of node: {type(node)}"
        raise ValueError(msg)

    def visit_Name(self, node: ast.Name) -> Any:
        if node.id in self.context:
            return self.context[node.id]
        return node.id

    def visit_Attribute(self, node: ast.Attribute) -> Any:
        qualified_name = f"{self.visit(node.value)}.{node.attr}"
        if qualified_name in self.context:
            return self.context[qualified_name]

        value = self.visit(node.value)
        # Handle Enum member access
        if isinstance(value, dict):
            member_name = node.attr
            if member_name in value:
                return value[member_name]
            self._error(f"Enum member '{member_name}' not found in enum.")

        if isinstance(value, str) and value in self.context:
            enum_def = self.context[value]
            if isinstance(enum_def, dict):
                member_name = node.attr
                if member_name in enum_def:
                    return enum_def[member_name]
                self._error(f"Enum member '{member_name}' not found in enum '{value}'.")

        return qualified_name

    def visit_Subscript(self, node: ast.Subscript) -> Any:
        value = self.visit(node.value)
        slice_ = self.visit(node.slice)
        if isinstance(value, list) and isinstance(slice_, int):
            if slice_ < 0:
                msg = "Negative indices not supported in PineScript"
                raise ValueError(msg)
            # PineScript: series[0] is current, series[1] is previous
            index = -(slice_ + 1)
            if abs(index) > len(value):
                return None  # PineScript returns na for out of bounds
            return value[index]
        else:
            value_type = type(value)
            slice_type = type(slice_)
            msg = f"Subscript not supported for {value_type} with {slice_type}"
            raise NotImplementedError(msg)

    def _alma(
        self,
        series: list,
        period: int,
        offset: float,
        sigma: float,
    ) -> float:
        if len(series) < period:
            return 0.0
        
        # Calculate weights using Gaussian distribution
        m = offset * (period - 1)
        s = period / sigma
        
        weights = []
        weight_sum = 0.0
        
        for i in range(period):
            weight = math.exp(-((i - m) ** 2) / (2 * s ** 2))
            weights.append(weight)
            weight_sum += weight
        
        # Normalize weights
        weights = [w / weight_sum for w in weights]
        
        # Calculate ALMA
        alma = 0.0
        for i in range(period):
            alma += series[-(period - i)] * weights[i]
        
        return alma

    def _barssince(self, condition: list) -> int:
        if not condition:
            return 0
        
        # Count bars since last true condition
        for i in range(len(condition) - 1, -1, -1):
            if condition[i]:
                return len(condition) - 1 - i
        return len(condition)  # If no true condition found

    def _bbw(self, series: list, period: int, multiplier: float) -> float:
        if len(series) < period:
            return 0.0
        
        # Calculate Bollinger Bands
        sma = statistics.mean(series[-period:])
        stdev = statistics.stdev(series[-period:])
        upper = sma + (multiplier * stdev)
        lower = sma - (multiplier * stdev)
        
        # Bollinger Band Width = (upper - lower) / sma
        if sma == 0:
            return 0.0
        return (upper - lower) / sma

    def _cmo(self, series: list, period: int) -> float:
        if len(series) < period + 1:
            return 0.0
        
        # Calculate price changes
        changes = [series[i] - series[i-1] for i in range(1, len(series))]
        
        # Calculate gains and losses
        gains = [max(change, 0) for change in changes[-period:]]
        losses = [abs(min(change, 0)) for change in changes[-period:]]
        
        sum_gains = sum(gains)
        sum_losses = sum(losses)
        
        if sum_gains + sum_losses == 0:
            return 0.0
        
        # Chande Momentum Oscillator
        # = (sum_gains - sum_losses) / (sum_gains + sum_losses) * 100
        cmo = ((sum_gains - sum_losses) / (sum_gains + sum_losses)) * 100
        return cmo

    def _correlation(self, series1: list, series2: list, period: int) -> float:
        if len(series1) < period or len(series2) < period:
            return 0.0
        
        s1_window = series1[-period:]
        s2_window = series2[-period:]
        
        # Calculate correlation coefficient
        try:
            correlation = statistics.correlation(s1_window, s2_window)
            return correlation
        except statistics.StatisticsError:
            return 0.0

    def _cross(self, series1: list, series2) -> bool:
        min_length = 2
        if len(series1) < min_length:
            return False
        
        # Handle series2 being a scalar or series
        if isinstance(series2, (int, float)):
            s2_val = series2
            s2_prev = series2
        else:
            if len(series2) < min_length:
                return False
            s2_val = series2[-1]
            s2_prev = series2[-2]
        
        s1_val = series1[-1]
        s1_prev = series1[-2]
        
        # Check if they crossed: different signs in (s1 - s2)
        # for current and previous bars
        prev_diff = s1_prev - s2_prev
        curr_diff = s1_val - s2_val
        
        return prev_diff * curr_diff < 0

    def _falling(self, series: list, length: int) -> bool:
        if len(series) < length:
            return False
        
        # Check if the series has been falling for 'length' bars
        for i in range(1, length + 1):
            if series[-i] >= series[-(i + 1)]:
                return False
        return True

    def _highestbars(self, series: list, period: int) -> int:
        if len(series) < period:
            return 0
        
        # Find the highest value in the last 'period' bars
        window = series[-period:]
        max_value = max(window)
        
        # Find how many bars ago the highest value occurred
        for i in range(len(window) - 1, -1, -1):
            if window[i] == max_value:
                return len(window) - 1 - i
        return 0

    def _lowestbars(self, series: list, period: int) -> int:
        if len(series) < period:
            return 0
        
        # Find the lowest value in the last 'period' bars
        window = series[-period:]
        min_value = min(window)
        
        # Find how many bars ago the lowest value occurred
        for i in range(len(window) - 1, -1, -1):
            if window[i] == min_value:
                return len(window) - 1 - i
        return 0

    def _rising(self, series: list, length: int) -> bool:
        if len(series) < length:
            return False
        
        # Check if the series has been rising for 'length' bars
        for i in range(1, length + 1):
            if series[-i] <= series[-(i + 1)]:
                return False
        return True

    def _rma(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        
        # RMA (Running Moving Average) uses alpha = 1/period
        alpha = 1.0 / period
        rma = series[0]
        
        for price in series[1:]:
            rma = alpha * price + (1 - alpha) * rma
        
        return rma

    def _vwap(self, highs: list, lows: list, closes: list, volumes: list) -> float:
        min_len = 1
        if (len(highs) < min_len or len(lows) < min_len or
            len(closes) < min_len or len(volumes) < min_len):
            return 0.0
        
        # Ensure all series have the same length
        series_len = min(len(highs), len(lows), len(closes), len(volumes))
        
        cumulative_price_volume = 0.0
        cumulative_volume = 0.0
        
        for i in range(series_len):
            # Typical price = (high + low + close) / 3
            typical_price = (highs[i] + lows[i] + closes[i]) / 3
            cumulative_price_volume += typical_price * volumes[i]
            cumulative_volume += volumes[i]
        
        if cumulative_volume == 0:
            return 0.0
        
        return cumulative_price_volume / cumulative_volume

    def _vwma(self, series: list, volumes: list, period: int) -> float:
        if len(series) < period or len(volumes) < period:
            return 0.0
        
        # Calculate VWMA for the last 'period' bars
        price_volume_sum = 0.0
        volume_sum = 0.0
        
        for i in range(period):
            idx = -(period - i)
            price_volume_sum += series[idx] * volumes[idx]
            volume_sum += volumes[idx]
        
        if volume_sum == 0:
            return 0.0
        
        return price_volume_sum / volume_sum

    def _hma(self, series: list, period: int) -> float:
        if len(series) < period:
            return 0.0
        
        # Hull Moving Average calculation
        # Step 1: WMA with period/2
        half_period = max(period // 2, 1)
        
        wma_half = self._wma(series, half_period)
        
        # Step 2: WMA with full period
        wma_full = self._wma(series, period)
        
        # Step 3: 2 * WMA(half) - WMA(full)
        diff_series = []
        for i in range(len(wma_half)):
            if i < len(wma_full):
                diff_series.append(2 * wma_half[i] - wma_full[i])
            else:
                diff_series.append(2 * wma_half[i])
        
        # Step 4: WMA of the difference with sqrt(period)
        sqrt_period = max(int(math.sqrt(period)), 1)
        
        return self._wma(diff_series, sqrt_period)

    def _sar_full(
        self,
        highs: list,
        lows: list,
        closes: list,
        accel: float,
        max_accel: float,
        increment: float,
    ) -> list:
        # Parabolic SAR calculation
        # Reference: https://www.investopedia.com/terms/p/parabolic.asp

        if len(highs) != len(lows) or len(highs) != len(closes):
            self._error("Highs, lows, and closes lists must have the same length.")

        sar = [0] * len(closes)
        trend = 1  # 1 = uptrend, -1 = downtrend
        af = accel  # Acceleration factor
        ep = highs[0]  # Extreme point

        for i in range(1, len(closes)):
            if trend == 1:
                sar[i] = sar[i - 1] + af * (ep - sar[i - 1])
                sar[i] = min(sar[i], lows[i - 1], lows[i])  # Stop at the previous low
                if highs[i] > ep:
                    ep = highs[i]
                    af = min(af + accel, max_accel)  # Increase AF, cap at max_accel
            else:
                sar[i] = sar[i - 1] + af * (ep - sar[i - 1])
                sar[i] = max(sar[i], highs[i - 1], highs[i])  # Stop at the previous high
                if lows[i] < ep:
                    ep = lows[i]
                    af = min(af + accel, max_accel)  # Increase AF, cap at max_accel

            # Reverse the trend
            if (trend == 1 and sar[i] > highs[i]) or (trend == -1 and sar[i] < lows[i]):
                trend *= -1
                sar[i] = ep  # Jump to the extreme point

        return sar

    def _sar(self, highs: list, lows: list, closes: list) -> float:
        # Call the full SAR implementation and return the last value
        sar_values = self._sar_full(highs, lows, closes, 0.02, 0.02, 0.02)
        return sar_values[-1] if sar_values else 0.0

    def _tsi(self, series: list, long_period: int, short_period: int) -> float:
        if len(series) < long_period + short_period:
            return 0.0
        
        # Calculate momentum
        momentum = [series[i] - series[i-1] for i in range(1, len(series))]
        
        # Double smooth momentum
        ema_short_momentum = self._ema(momentum[-long_period:], short_period)
        ema_long_momentum = self._ema(ema_short_momentum, long_period)
        
        # Double smooth absolute momentum
        abs_momentum = [abs(m) for m in momentum]
        ema_short_abs = self._ema(abs_momentum[-long_period:], short_period)
        ema_long_abs = self._ema(ema_short_abs, long_period)
        
        if not ema_long_abs or ema_long_abs[-1] == 0:
            return 0.0
        
        # TSI = 100 * (double_smoothed_momentum / double_smoothed_abs_momentum)
        tsi = 100 * (ema_long_momentum[-1] / ema_long_abs[-1])
        return tsi

    def _wma(self, series: list, period: int) -> list:
        if len(series) < period:
            return []
        
        result = []
        for i in range(period - 1, len(series)):
            window = series[i - period + 1:i + 1]
            weights = list(range(1, period + 1))
            weighted_sum = sum(
                w * val for w, val in zip(weights, window, strict=True)
            )
            total_weight = sum(weights)
            wma = weighted_sum / total_weight
            result.append(wma)
        
        return result
