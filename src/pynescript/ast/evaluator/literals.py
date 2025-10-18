from __future__ import annotations

from typing import Any

from pynescript.ast import node as ast


class LiteralEvaluator:

    def visit_Constant(self, node: ast.Constant):
        if node.kind:
            msg = f"unexpected constant kind: {node.kind!s}"
            raise ValueError(msg)
        return node.value

    def visit_Tuple(self, node: ast.Tuple) -> Any:
        return [self.visit(elt) for elt in node.elts]
