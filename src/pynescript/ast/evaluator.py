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

    def _call_builtin(self, name: str, args):
        builtins = {
            "math.max": lambda: max(args),
            "math.min": lambda: min(args),
            "math.abs": (
                lambda: abs(args[0]) if len(args) == 1 else self._error("math.abs takes exactly one argument")
            ),
            "math.sqrt": (
                lambda: math.sqrt(args[0]) if len(args) == 1 else self._error("math.sqrt takes exactly one argument")
            ),
            "math.round": (
                lambda: (
                    round(args[0])
                    if len(args) == 1
                    else round(args[0], args[1])
                    if len(args) == 2
                    else self._error("math.round takes one or two arguments")
                )
            ),
            "math.floor": (
                lambda: math.floor(args[0]) if len(args) == 1 else self._error("math.floor takes exactly one argument")
            ),
            "math.ceil": (
                lambda: math.ceil(args[0]) if len(args) == 1 else self._error("math.ceil takes exactly one argument")
            ),
            "math.pow": (
                lambda: math.pow(args[0], args[1])
                if len(args) == 2
                else self._error("math.pow takes exactly two arguments")
            ),
            "math.log": (
                lambda: (
                    math.log(args[0])
                    if len(args) == 1
                    else math.log(args[0], args[1])
                    if len(args) == 2
                    else self._error("math.log takes one or two arguments")
                )
            ),
            "math.sin": (
                lambda: math.sin(args[0]) if len(args) == 1 else self._error("math.sin takes exactly one argument")
            ),
            "math.cos": (
                lambda: math.cos(args[0]) if len(args) == 1 else self._error("math.cos takes exactly one argument")
            ),
            "math.tan": (
                lambda: math.tan(args[0]) if len(args) == 1 else self._error("math.tan takes exactly one argument")
            ),
            "math.acos": (
                lambda: math.acos(args[0])
                if len(args) == 1
                else self._error("math.acos takes exactly one argument")
            ),
            "math.asin": (
                lambda: math.asin(args[0])
                if len(args) == 1
                else self._error("math.asin takes exactly one argument")
            ),
            "math.atan": (
                lambda: math.atan(args[0])
                if len(args) == 1
                else self._error("math.atan takes exactly one argument")
            ),
            "math.exp": (
                lambda: math.exp(args[0])
                if len(args) == 1
                else self._error("math.exp takes exactly one argument")
            ),
            "math.log10": (
                lambda: math.log10(args[0])
                if len(args) == 1
                else self._error("math.log10 takes exactly one argument")
            ),
            "math.sign": (
                lambda: (1 if args[0] > 0 else -1 if args[0] < 0 else 0)
                if len(args) == 1
                else self._error("math.sign takes exactly one argument")
            ),
            "math.sum": (
                lambda: sum(args[0])
                if len(args) == 1 and isinstance(args[0], list)
                else self._error("math.sum takes exactly one array argument")
            ),
            "math.avg": (
                lambda: statistics.mean(args[0])
                if len(args) == 1 and isinstance(args[0], list) and args[0]
                else self._error("math.avg takes exactly one non-empty array argument")
            ),
            "math.todegrees": (
                lambda: math.degrees(args[0])
                if len(args) == 1
                else self._error("math.todegrees takes exactly one argument")
            ),
            "math.toradians": (
                lambda: math.radians(args[0])
                if len(args) == 1
                else self._error("math.toradians takes exactly one argument")
            ),
            "str.length": (
                lambda: len(args[0])
                if len(args) == 1 and isinstance(args[0], str)
                else self._error("str.length takes exactly one string argument")
            ),
            "str.upper": (
                lambda: args[0].upper()
                if len(args) == 1 and isinstance(args[0], str)
                else self._error("str.upper takes exactly one string argument")
            ),
            "str.lower": (
                lambda: args[0].lower()
                if len(args) == 1 and isinstance(args[0], str)
                else self._error("str.lower takes exactly one string argument")
            ),
            "str.contains": (
                lambda: args[1] in args[0]
                if (len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str))
                else self._error("str.contains takes two string arguments")
            ),
            "str.startswith": (
                lambda: args[0].startswith(args[1])
                if (len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str))
                else self._error("str.startswith takes two string arguments")
            ),
            "str.substring": (
                lambda: (
                    args[0][args[1] :]
                    if (len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], int))
                    else args[0][args[1] : args[2]]
                    if (
                        len(args) == 3
                        and isinstance(args[0], str)
                        and isinstance(args[1], int)
                        and isinstance(args[2], int)
                    )
                    else self._error("str.substring takes string and 1-2 ints")
                )
            ),
            "str.endswith": (
                lambda: args[0].endswith(args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                )
                else self._error("str.endswith takes two string arguments")
            ),
            "str.repeat": (
                lambda: args[0] * args[1]
                if (
                    len(args) == 2
                    and isinstance(args[0], str)
                    and isinstance(args[1], int)
                )
                else self._error("str.repeat takes string and int")
            ),
            "str.replace": (
                lambda: args[0].replace(args[1], args[2], 1)
                if (
                    len(args) == 3
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                    and isinstance(args[2], str)
                )
                else self._error("str.replace takes three string arguments")
            ),
            "str.replace_all": (
                lambda: args[0].replace(args[1], args[2])
                if (
                    len(args) == 3
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                    and isinstance(args[2], str)
                )
                else self._error("str.replace_all takes three string arguments")
            ),
            "str.split": (
                lambda: (
                    args[0].split(args[1])
                    if (
                        len(args) == 2
                        and isinstance(args[0], str)
                        and isinstance(args[1], str)
                    )
                    else args[0].split()
                    if len(args) == 1 and isinstance(args[0], str)
                    else self._error("str.split takes string and optional separator")
                )
            ),
            "str.trim": (
                lambda: args[0].strip()
                if len(args) == 1 and isinstance(args[0], str)
                else self._error("str.trim takes exactly one string argument")
            ),
            "str.tonumber": (
                lambda: float(args[0])
                if len(args) == 1 and isinstance(args[0], str)
                else self._error("str.tonumber takes exactly one string argument")
            ),
            "str.tostring": (
                lambda: str(args[0])
                if len(args) == 1
                else self._error("str.tostring takes exactly one argument")
            ),
            "array.size": (
                lambda: len(args[0])
                if len(args) == 1 and isinstance(args[0], list)
                else self._error("array.size takes exactly one array argument")
            ),
            "array.get": (
                lambda: args[0][args[1]]
                if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                else self._error("array.get takes array and index")
            ),
            "array.push": (
                lambda: args[0] + [args[1]]
                if len(args) == 2 and isinstance(args[0], list)
                else self._error("array.push takes array and value")
            ),
            "array.pop": (
                lambda: args[0][:-1]
                if len(args) == 1 and isinstance(args[0], list) and len(args[0]) > 0
                else self._error("array.pop takes non-empty array")
            ),
            "array.slice": (
                lambda: args[0][args[1] : args[2]]
                if (
                    len(args) == 3
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and isinstance(args[2], int)
                )
                else self._error("array.slice takes array, start, end")
            ),
            "color.new": (
                lambda: f"color({args[0]})" if len(args) == 1 else self._error("color.new takes one argument")
            ),
            "ta.sma": (
                lambda: (
                    statistics.mean(args[0][-args[1] :])
                    if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                    else self._error("ta.sma takes series and period")
                )
            ),
            "ta.ema": (
                lambda: self._ema(args[0], args[1])
                if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                else self._error("ta.ema takes series and period")
            ),
            "ta.rsi": (
                lambda: self._rsi(args[0], args[1])
                if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                else self._error("ta.rsi takes series and period")
            ),
            "ta.stdev": (
                lambda: (
                    statistics.stdev(args[0][-args[1] :])
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                        and len(args[0][-args[1] :]) > 1
                    )
                    else self._error("ta.stdev takes series and period")
                )
            ),
            "ta.change": (
                lambda: (
                    args[0][-1] - args[0][-args[1] - 1]
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                        and len(args[0]) > args[1]
                    )
                    else self._error("ta.change takes series and period")
                )
            ),
            "ta.highest": (
                lambda: (
                    max(args[0][-args[1] :])
                    if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                    else self._error("ta.highest takes series and period")
                )
            ),
            "ta.lowest": (
                lambda: (
                    min(args[0][-args[1] :])
                    if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                    else self._error("ta.lowest takes series and period")
                )
            ),
            "ta.range": (
                lambda: (
                    max(args[0][-args[1] :]) - min(args[0][-args[1] :])
                    if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                    else self._error("ta.range takes series and period")
                )
            ),
            "ta.wma": (
                lambda: self._wma(args[0], args[1])
                if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                else self._error("ta.wma takes series and period")
            ),
            "ta.bb": (
                lambda: self._bollinger_bands(args[0], args[1], args[2])
                if (
                    len(args) == 3
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and isinstance(args[2], (int, float))
                )
                else self._error("ta.bb takes series, period, and multiplier")
            ),
            "ta.macd": (
                lambda: self._macd(args[0], args[1], args[2], args[3])
                if (
                    len(args) == 4
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and isinstance(args[2], int)
                    and isinstance(args[3], int)
                )
                else self._error("ta.macd takes series, fast, slow, signal")
            ),
            "ta.atr": (
                lambda: self._atr(args[0], args[1], args[2], args[3])
                if (
                    len(args) == 4
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], int)
                )
                else self._error("ta.atr takes highs, lows, closes, period")
            ),
            "ta.crossover": (
                lambda: (
                    args[0][-1] > args[1][-1] and args[0][-2] <= args[1][-2]
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], (list, int, float))
                        and len(args[0]) >= 2
                    )
                    else self._error("ta.crossover takes two series")
                )
            ),
            "ta.crossunder": (
                lambda: (
                    args[0][-1] < args[1][-1] and args[0][-2] >= args[1][-2]
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], (list, int, float))
                        and len(args[0]) >= 2
                    )
                    else self._error("ta.crossunder takes two series")
                )
            ),
            "ta.stoch": (
                lambda: self._stoch(args[0], args[1], args[2], args[3], args[4])
                if (
                    len(args) == 5
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], int)
                    and isinstance(args[4], int)
                )
                else self._error("ta.stoch takes highs, lows, closes, k_period, d_period")
            ),
            "ta.adx": (
                lambda: self._adx(args[0], args[1], args[2], args[3])
                if (
                    len(args) == 4
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], int)
                )
                else self._error("ta.adx takes highs, lows, closes, period")
            ),
            "ta.cci": (
                lambda: self._cci(args[0], args[1], args[2], args[3])
                if (
                    len(args) == 4
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], int)
                )
                else self._error("ta.cci takes highs, lows, closes, period")
            ),
            "ta.roc": (
                lambda: self._roc(args[0], args[1])
                if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], int))
                else self._error("ta.roc takes series and period")
            ),
            "ta.wpr": (
                lambda: self._wpr(args[0], args[1], args[2], args[3])
                if (
                    len(args) == 4
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], int)
                )
                else self._error("ta.wpr takes highs, lows, closes, period")
            ),
            "ta.obv": (
                lambda: self._obv(args[0], args[1])
                if (len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], list))
                else self._error("ta.obv takes closes and volumes")
            ),
            "ta.mfi": (
                lambda: self._mfi(args[0], args[1], args[2], args[3], args[4])
                if (
                    len(args) == 5
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], list)
                    and isinstance(args[3], list)
                    and isinstance(args[4], int)
                )
                else self._error("ta.mfi takes highs, lows, closes, volumes, period")
            ),
            "ta.cum": (
                lambda: self._cum(args[0])
                if (len(args) == 1 and isinstance(args[0], list))
                else self._error("ta.cum takes a series")
            ),
            "ta.dev": (
                lambda: self._dev(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.dev takes series and period")
            ),
            "ta.max": (
                lambda: self._max(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.max takes series and period")
            ),
            "ta.min": (
                lambda: self._min(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.min takes series and period")
            ),
            "ta.mom": (
                lambda: self._mom(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.mom takes series and period")
            ),
            "ta.median": (
                lambda: self._median(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.median takes series and period")
            ),
            "ta.mode": (
                lambda: self._mode(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.mode takes series and period")
            ),
            "ta.percentrank": (
                lambda: self._percentrank(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.percentrank takes series and period")
            ),
            "ta.variance": (
                lambda: self._variance(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.variance takes series and period")
            ),
            "ta.valuewhen": (
                lambda: self._valuewhen(args[0], args[1], args[2])
                if (
                    len(args) == 3
                    and isinstance(args[0], list)
                    and isinstance(args[1], list)
                    and isinstance(args[2], int)
                )
                else self._error("ta.valuewhen takes condition, source, occurrence")
            ),
            "na": lambda: None,
            "nz": (
                lambda: args[1]
                if args[0] is None
                else args[0]
                if len(args) == 2
                else args[0]
                if args[0] is not None
                else 0
                if len(args) == 1
                else self._error("nz takes 1 or 2 arguments")
            ),
            "bool": (lambda: bool(args[0]) if len(args) == 1 else self._error("bool takes one argument")),
            "int": (lambda: int(args[0]) if len(args) == 1 else self._error("int takes one argument")),
            "float": (lambda: float(args[0]) if len(args) == 1 else self._error("float takes one argument")),
        }
        if name in builtins:
            return builtins[name]()
        else:
            msg = f"Unknown built-in function: {name}"
            raise ValueError(msg)

    def _error(self, msg: str):
        raise ValueError(msg)

    def _ema(self, series: list, period: int) -> float:
        """Calculate Exponential Moving Average."""
        if not series or period <= 0:
            return 0.0
        multiplier = 2 / (period + 1)
        ema = series[0] if len(series) > 0 else 0.0
        for price in series[1:]:
            ema = (price * multiplier) + (ema * (1 - multiplier))
        return ema

    def _rsi(self, series: list, period: int) -> float:
        """Calculate Relative Strength Index."""
        if len(series) < period + 1:
            return 50.0
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

    def _wma(self, series: list, period: int) -> float:
        """Calculate Weighted Moving Average."""
        if len(series) < period:
            return 0.0
        data = series[-period:]
        weights = list(range(1, period + 1))
        weighted_sum = sum(d * w for d, w in zip(data, weights, strict=True))
        return weighted_sum / sum(weights)

    def _bollinger_bands(self, series: list, period: int, mult: float):
        """Calculate Bollinger Bands (middle, upper, lower)."""
        if len(series) < period:
            return [0.0, 0.0, 0.0]
        data = series[-period:]
        middle = statistics.mean(data)
        std = statistics.stdev(data) if len(data) > 1 else 0.0
        upper = middle + (mult * std)
        lower = middle - (mult * std)
        return [middle, upper, lower]

    def _macd(self, series: list, fast: int, slow: int, signal: int):
        """Calculate MACD (macd, signal, histogram)."""
        if len(series) < slow:
            return [0.0, 0.0, 0.0]
        fast_ema = self._ema(series, fast)
        slow_ema = self._ema(series, slow)
        macd = fast_ema - slow_ema
        signal_line = self._ema([macd], signal)  # EMA of MACD values, but need history
        # For simplicity, approximate signal as EMA of recent MACD
        hist = macd - signal_line
        return [macd, signal_line, hist]

    def _atr(self, highs: list, lows: list, closes: list, period: int) -> float:
        """Calculate Average True Range."""
        if len(highs) < 2 or len(lows) < 2 or len(closes) < 2:
            return 0.0
        tr_values = []
        for i in range(1, len(highs)):
            hl = highs[i] - lows[i]
            hc = abs(highs[i] - closes[i - 1])
            lc = abs(lows[i] - closes[i - 1])
            tr = max(hl, hc, lc)
            tr_values.append(tr)
        if len(tr_values) < period:
            return statistics.mean(tr_values) if tr_values else 0.0
        return self._ema(tr_values, period)

    def _stoch(self, highs: list, lows: list, closes: list, k_period: int, d_period: int):
        """Calculate Stochastic Oscillator (%K, %D)."""
        if len(highs) < k_period or len(lows) < k_period or len(closes) < k_period:
            return [0.0, 0.0]

        # Calculate %K values
        k_values = []
        for i in range(k_period - 1, len(closes)):
            high_win = highs[i - k_period + 1 : i + 1]
            low_win = lows[i - k_period + 1 : i + 1]
            high_max = max(high_win)
            low_min = min(low_win)
            close_curr = closes[i]

            if high_max == low_min:
                k = 100.0  # Avoid division by zero
            else:
                k = 100.0 * (close_curr - low_min) / (high_max - low_min)
            k_values.append(k)

        # %K is the last calculated value
        k = k_values[-1] if k_values else 0.0

        # %D is SMA of %K over d_period
        if len(k_values) < d_period:
            d = statistics.mean(k_values) if k_values else 0.0
        else:
            d = statistics.mean(k_values[-d_period:])

        return [k, d]

    def _adx(self, highs: list, lows: list, closes: list, period: int) -> float:
        """Calculate Average Directional Index (ADX)."""
        min_len = period + 1
        if len(highs) < min_len or len(lows) < min_len or len(closes) < min_len:
            return 0.0

        # Calculate True Range, +DM, -DM
        tr_values = []
        plus_dm_values = []
        minus_dm_values = []

        for i in range(1, len(highs)):
            # True Range
            hl = highs[i] - lows[i]
            hc = abs(highs[i] - closes[i - 1])
            lc = abs(lows[i] - closes[i - 1])
            tr = max(hl, hc, lc)
            tr_values.append(tr)

            # Directional Movement
            high_diff = highs[i] - highs[i - 1]
            low_diff = lows[i - 1] - lows[i]

            plus_dm = high_diff if high_diff > low_diff and high_diff > 0 else 0.0
            minus_dm = low_diff if low_diff > high_diff and low_diff > 0 else 0.0

            plus_dm_values.append(plus_dm)
            minus_dm_values.append(minus_dm)

        if len(tr_values) < period:
            return 0.0

        # Calculate smoothed values using EMA
        tr_ema = self._ema(tr_values, period)
        plus_dm_ema = self._ema(plus_dm_values, period)
        minus_dm_ema = self._ema(minus_dm_values, period)

        # Calculate Directional Indicators
        plus_di = 100.0 * plus_dm_ema / tr_ema if tr_ema != 0 else 0.0
        minus_di = 100.0 * minus_dm_ema / tr_ema if tr_ema != 0 else 0.0

        # Calculate DX
        di_sum = plus_di + minus_di
        di_diff = abs(plus_di - minus_di)
        dx = 100.0 * di_diff / di_sum if di_sum != 0 else 0.0

        # Calculate ADX as EMA of DX
        dx_values = [dx]  # For simplicity, use current DX as single value
        adx = self._ema(dx_values, period)

        return adx

    def _cci(self, highs: list, lows: list, closes: list, period: int) -> float:
        """Calculate Commodity Channel Index (CCI)."""
        if len(highs) < period or len(lows) < period or len(closes) < period:
            return 0.0

        # Calculate Typical Price for each period
        typical_prices = []
        for i in range(len(highs)):
            tp = (highs[i] + lows[i] + closes[i]) / 3.0
            typical_prices.append(tp)

        # Calculate SMA of Typical Price
        if len(typical_prices) < period:
            return 0.0

        sma_tp = statistics.mean(typical_prices[-period:])

        # Calculate Mean Deviation
        deviations = [abs(tp - sma_tp) for tp in typical_prices[-period:]]
        mean_dev = statistics.mean(deviations) if deviations else 0.0

        # Calculate CCI
        if mean_dev == 0:
            return 0.0

        cci = (typical_prices[-1] - sma_tp) / (0.015 * mean_dev)
        return cci

    def _roc(self, series: list, period: int) -> float:
        """Calculate Rate of Change (ROC)."""
        if len(series) < period + 1:
            return 0.0

        current = series[-1]
        past = series[-(period + 1)]

        if past == 0:
            return 0.0

        roc = ((current - past) / past) * 100.0
        return roc

    def _wpr(self, highs: list, lows: list, closes: list, period: int) -> float:
        """Calculate Williams %R."""
        if len(highs) < period or len(lows) < period or len(closes) < period:
            return 0.0

        # Get highest high and lowest low over the period
        high_window = highs[-period:]
        low_window = lows[-period:]
        highest_high = max(high_window)
        lowest_low = min(low_window)
        current_close = closes[-1]

        if highest_high == lowest_low:
            return -50.0  # Neutral value when range is zero

        wpr = ((highest_high - current_close) / (highest_high - lowest_low)) * -100.0
        return wpr

    def _obv(self, closes: list, volumes: list) -> float:
        """Calculate On Balance Volume (OBV)."""
        if len(closes) < 2 or len(volumes) < 2:
            return 0.0

        obv = 0.0
        for i in range(1, len(closes)):
            if closes[i] > closes[i - 1]:
                obv += volumes[i]
            elif closes[i] < closes[i - 1]:
                obv -= volumes[i]
            # If closes[i] == closes[i-1], OBV remains unchanged

        return obv

    def _mfi(self, highs: list, lows: list, closes: list, volumes: list, period: int) -> float:
        """Calculate Money Flow Index (MFI)."""
        if len(highs) < period or len(lows) < period or len(closes) < period or len(volumes) < period:
            return 0.0

        # Calculate Typical Price and Raw Money Flow
        typical_prices = []
        money_flows = []

        for i in range(len(highs)):
            tp = (highs[i] + lows[i] + closes[i]) / 3.0
            typical_prices.append(tp)

            if i > 0:
                if tp > typical_prices[i - 1]:
                    money_flows.append(tp * volumes[i])  # Positive money flow
                elif tp < typical_prices[i - 1]:
                    money_flows.append(-tp * volumes[i])  # Negative money flow
                else:
                    money_flows.append(0.0)  # No money flow

        # Calculate Money Flow Ratio
        if len(money_flows) < period:
            return 0.0

        positive_flow = sum(mf for mf in money_flows[-period:] if mf > 0)
        negative_flow = abs(sum(mf for mf in money_flows[-period:] if mf < 0))

        if negative_flow == 0:
            return 100.0  # All positive flow

        money_flow_ratio = positive_flow / negative_flow
        mfi = 100.0 - (100.0 / (1.0 + money_flow_ratio))
        return mfi

    def _cum(self, series: list) -> float:
        """Calculate cumulative sum of series."""
        if not series:
            return 0.0
        return sum(series)

    def _dev(self, series: list, period: int) -> float:
        """Calculate standard deviation from mean over period."""
        if len(series) < period:
            return 0.0
        recent_values = series[-period:]
        mean_val = statistics.mean(recent_values)
        if len(recent_values) > 1:
            return statistics.stdev(recent_values, mean_val)
        return 0.0

    def _max(self, series: list, period: int) -> float:
        """Calculate maximum value over period."""
        if len(series) < period:
            return 0.0
        return max(series[-period:])

    def _min(self, series: list, period: int) -> float:
        """Calculate minimum value over period."""
        if len(series) < period:
            return 0.0
        return min(series[-period:])

    def _mom(self, series: list, period: int) -> float:
        """Calculate momentum (current value - value n periods ago)."""
        if len(series) < period + 1:
            return 0.0
        return series[-1] - series[-(period + 1)]

    def _median(self, series: list, period: int) -> float:
        """Calculate median value over period."""
        if len(series) < period:
            return 0.0
        recent_values = series[-period:]
        return statistics.median(recent_values)

    def _mode(self, series: list, period: int) -> float:
        """Calculate mode (most frequent value) over period."""
        if len(series) < period:
            return 0.0
        recent_values = series[-period:]
        try:
            return statistics.mode(recent_values)
        except statistics.StatisticsError:
            # Return the first value if there's no unique mode
            return recent_values[0]

    def _percentrank(self, series: list, period: int) -> float:
        """Calculate percentile rank over period."""
        if len(series) < period:
            return 0.0
        recent_values = series[-period:]
        current_value = recent_values[-1]
        # Count how many values are less than current
        count_less = sum(1 for v in recent_values if v < current_value)
        return (count_less / (len(recent_values) - 1)) * 100.0

    def _variance(self, series: list, period: int) -> float:
        """Calculate variance over period."""
        if len(series) < period:
            return 0.0
        recent_values = series[-period:]
        if len(recent_values) < 2:
            return 0.0
        return statistics.variance(recent_values)

    def _valuewhen(self, condition: list, source: list,
                   occurrence: int) -> float:
        """Return value from source series when condition was true."""
        if len(condition) != len(source) or occurrence < 1:
            return 0.0
        
        # Find occurrences where condition is true
        true_indices = [i for i, val in enumerate(condition) if val]
        
        if len(true_indices) < occurrence:
            return 0.0
            
        # Get the index of the nth occurrence (from the end)
        target_index = true_indices[-(occurrence)]
        return source[target_index]

    def generic_visit(self, node: ast.AST):
        msg = f"unexpected type of node: {type(node)}"
        raise ValueError(msg)

    def visit_Name(self, node: ast.Name) -> Any:
        if node.id in self.context:
            return self.context[node.id]
        return node.id

    def visit_Attribute(self, node: ast.Attribute) -> Any:
        return f"{self.visit(node.value)}.{node.attr}"

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
