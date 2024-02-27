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
import operator

from pynescript.ast import node as ast
from pynescript.ast.visitor import NodeVisitor


class NodeLiteralEvaluator(NodeVisitor):
    # ruff: noqa: N802

    def visit_BoolOp(self, node: ast.BoolOp):
        if isinstance(node.op, ast.And):
            return all(self.visit(value) for value in node.values)
        if isinstance(node.op, ast.Or):
            return any(self.visit(value) for value in node.values)
        msg = f"unexpected node operator: {node.op}"
        raise ValueError(msg)

    def visit_BinOp(self, node: ast.BinOp):
        if isinstance(node.op, ast.Add):
            return operator.add(self.visit(node.left), self.visit(node.right))
        if isinstance(node.op, ast.Sub):
            return operator.sub(self.visit(node.left), self.visit(node.right))
        if isinstance(node.op, ast.Mult):
            return operator.mul(self.visit(node.left), self.visit(node.right))
        if isinstance(node.op, ast.Div):
            return operator.truediv(self.visit(node.left), self.visit(node.right))
        if isinstance(node.op, ast.Mod):
            return operator.mod(self.visit(node.left), self.visit(node.right))
        msg = f"unexpected node operator: {node.op}"
        raise ValueError(msg)

    def visit_UnaryOp(self, node: ast.UnaryOp):
        if isinstance(node.op, ast.Not):
            return operator.not_(self.visit(node.operand))
        if isinstance(node.op, ast.UAdd):
            return operator.pos(self.visit(node.operand))
        if isinstance(node.op, ast.USub):
            return operator.neg(self.visit(node.operand))
        msg = f"unexpected node operator: {node.op}"
        raise ValueError(msg)

    def visit_Conditional(self, node: ast.Conditional):
        return self.visit(node.body) if self.visit(node.test) else self.visit(node.orelse)

    def visit_Compare(self, node: ast.Compare):  # noqa: C901, PLR0911, PLR0912
        left = self.visit(node.left)
        comparators = map(self.visit, itertools.chain([node.left], node.comparators))
        comparator_pairs = itertools.pairwise(comparators)
        compare_ops = map(self.visit, node.ops)
        for op, (left, right) in zip(compare_ops, comparator_pairs, strict=True):
            if isinstance(op, ast.Eq):
                if not operator.eq(left, right):
                    return False
            elif isinstance(op, ast.NotEq):
                if not operator.ne(left, right):
                    return False
            elif isinstance(op, ast.Lt):
                if not operator.lt(left, right):
                    return False
            elif isinstance(op, ast.LtE):
                if not operator.le(left, right):
                    return False
            elif isinstance(op, ast.Gt):
                if not operator.gt(left, right):
                    return False
            elif isinstance(op, ast.GtE):
                if not operator.ge(left, right):
                    return False
            else:
                msg = f"unexpected node operator: {op}"
                raise ValueError(msg)
        return True

    def visit_Constant(self, node: ast.Constant):
        if node.kind:
            msg = f"unexpected constant kind: {node.kind!s}"
            raise ValueError(msg)
        return node.value

    def visit_Tuple(self, node: ast.Tuple):
        return tuple(self.visit(elt) for elt in node.elts)

    def generic_visit(self, node: ast.AST):
        msg = f"unexpected type of node: {type(node)}"
        raise ValueError(msg)
