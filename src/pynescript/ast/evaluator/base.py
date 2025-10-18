from __future__ import annotations

import math

from typing import Any

from pynescript.ast import node as ast
from pynescript.ast.visitor import NodeVisitor


class BaseEvaluator(NodeVisitor):

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

    def generic_visit(self, node: ast.AST):
        msg = f"unexpected type of node: {type(node)}"
        raise ValueError(msg)

    def _error(self, msg: str):
        raise ValueError(msg)
