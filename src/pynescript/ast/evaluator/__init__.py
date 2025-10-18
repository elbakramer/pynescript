from __future__ import annotations

from .base import BaseEvaluator
from .builtins import BuiltinEvaluator
from .expressions import ExpressionEvaluator
from .literals import LiteralEvaluator
from .names import NameEvaluator
from .statements import StatementEvaluator


class NodeLiteralEvaluator(
    BaseEvaluator,
    LiteralEvaluator,
    ExpressionEvaluator,
    BuiltinEvaluator,
    StatementEvaluator,
    NameEvaluator,
):
    pass
