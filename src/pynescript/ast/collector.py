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

from pynescript.ast import node as ast
from pynescript.ast.visitor import NodeVisitor


Structure = (
    ast.ForTo,
    ast.ForIn,
    ast.While,
    ast.If,
    ast.Switch,
)


class StatementCollector(NodeVisitor):
    # ruff: noqa: N802

    def visit_Script(self, node):
        for stmt in node.body:
            yield from self.visit(stmt)

    def visit_FunctionDef(self, node):
        yield node
        for stmt in node.body:
            yield from self.visit(stmt)

    def visit_TypeDef(self, node):
        yield node
        for stmt in node.body:
            yield from self.visit(stmt)

    def visit_EnumDef(self, node):
        yield node
        for stmt in node.body:
            yield from self.visit(stmt)

    def visit_Assign(self, node):
        yield node
        if isinstance(node.value, Structure):
            yield from self.visit(node.value)

    def visit_ReAssign(self, node):
        yield node
        if isinstance(node.value, Structure):
            yield from self.visit(node.value)

    def visit_AugAssign(self, node):
        yield node
        if isinstance(node.value, Structure):
            yield from self.visit(node.value)

    def visit_Import(self, node):
        yield node

    def visit_Expr(self, node):
        yield node
        if isinstance(node.value, Structure):
            yield from self.visit(node.value)

    def visit_Break(self, node):
        yield node

    def visit_Continue(self, node):
        yield node

    def visit_ForTo(self, node):
        for stmt in node.body:
            yield from self.visit(stmt)

    def visit_ForIn(self, node):
        for stmt in node.body:
            yield from self.visit(stmt)

    def visit_While(self, node):
        for stmt in node.body:
            yield from self.visit(stmt)

    def visit_If(self, node):
        for stmt in node.body:
            yield from self.visit(stmt)
        for stmt in node.orelse:
            yield from self.visit(stmt)

    def visit_Switch(self, node):
        for case in node.cases:
            yield from self.visit(case)

    def visit_Case(self, node):
        for stmt in node.body:
            yield from self.visit(stmt)
