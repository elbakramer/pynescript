from __future__ import annotations

from pynescript.ast import node as ast


class StatementEvaluator:

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
