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
                lambda: abs(args[0])
                if len(args) == 1
                else self._error("math.abs takes exactly one argument")
            ),
            "math.sqrt": (
                lambda: math.sqrt(args[0])
                if len(args) == 1
                else self._error("math.sqrt takes exactly one argument")
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
                lambda: math.floor(args[0])
                if len(args) == 1
                else self._error("math.floor takes exactly one argument")
            ),
            "math.ceil": (
                lambda: math.ceil(args[0])
                if len(args) == 1
                else self._error("math.ceil takes exactly one argument")
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
                lambda: math.sin(args[0])
                if len(args) == 1
                else self._error("math.sin takes exactly one argument")
            ),
            "math.cos": (
                lambda: math.cos(args[0])
                if len(args) == 1
                else self._error("math.cos takes exactly one argument")
            ),
            "math.tan": (
                lambda: math.tan(args[0])
                if len(args) == 1
                else self._error("math.tan takes exactly one argument")
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
                if (
                    len(args) == 2
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                )
                else self._error("str.contains takes two string arguments")
            ),
            "str.startswith": (
                lambda: args[0].startswith(args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], str)
                    and isinstance(args[1], str)
                )
                else self._error("str.startswith takes two string arguments")
            ),
            "str.substring": (
                lambda: (
                    args[0][args[1]:]
                    if (
                        len(args) == 2
                        and isinstance(args[0], str)
                        and isinstance(args[1], int)
                    )
                    else args[0][args[1]:args[2]]
                    if (
                        len(args) == 3
                        and isinstance(args[0], str)
                        and isinstance(args[1], int)
                        and isinstance(args[2], int)
                    )
                    else self._error("str.substring takes string and 1-2 ints")
                )
            ),
            "array.size": (
                lambda: len(args[0])
                if len(args) == 1 and isinstance(args[0], list)
                else self._error("array.size takes exactly one array argument")
            ),
            "array.get": (
                lambda: args[0][args[1]]
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
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
                lambda: args[0][args[1]:args[2]]
                if (
                    len(args) == 3
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                    and isinstance(args[2], int)
                )
                else self._error("array.slice takes array, start, end")
            ),
            "color.new": (
                lambda: f"color({args[0]})"
                if len(args) == 1
                else self._error("color.new takes one argument")
            ),
            "ta.sma": (
                lambda: (
                    statistics.mean(args[0][-args[1]:])
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                    )
                    else self._error("ta.sma takes series and period")
                )
            ),
            "ta.ema": (
                lambda: self._ema(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.ema takes series and period")
            ),
            "ta.rsi": (
                lambda: self._rsi(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
                else self._error("ta.rsi takes series and period")
            ),
            "ta.stdev": (
                lambda: (
                    statistics.stdev(args[0][-args[1]:])
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                        and len(args[0][-args[1]:]) > 1
                    )
                    else self._error("ta.stdev takes series and period")
                )
            ),
            "ta.change": (
                lambda: (
                    args[0][-1] - args[0][-args[1]-1]
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
                    max(args[0][-args[1]:])
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                    )
                    else self._error("ta.highest takes series and period")
                )
            ),
            "ta.lowest": (
                lambda: (
                    min(args[0][-args[1]:])
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                    )
                    else self._error("ta.lowest takes series and period")
                )
            ),
            "ta.range": (
                lambda: (
                    max(args[0][-args[1]:]) - min(args[0][-args[1]:])
                    if (
                        len(args) == 2
                        and isinstance(args[0], list)
                        and isinstance(args[1], int)
                    )
                    else self._error("ta.range takes series and period")
                )
            ),
            "ta.wma": (
                lambda: self._wma(args[0], args[1])
                if (
                    len(args) == 2
                    and isinstance(args[0], list)
                    and isinstance(args[1], int)
                )
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
                else self._error("ta.stoch takes highs, lows, closes, "
                                 "k_period, d_period")
            ),
            "na": lambda: None,
            "nz": (
                lambda: args[1] if args[0] is None else args[0]
                if len(args) == 2
                else args[0] if args[0] is not None else 0
                if len(args) == 1
                else self._error("nz takes 1 or 2 arguments")
            ),
            "bool": (
                lambda: bool(args[0])
                if len(args) == 1
                else self._error("bool takes one argument")
            ),
            "int": (
                lambda: int(args[0])
                if len(args) == 1
                else self._error("int takes one argument")
            ),
            "float": (
                lambda: float(args[0])
                if len(args) == 1
                else self._error("float takes one argument")
            ),
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
        changes = [series[i] - series[i-1] for i in range(1, len(series))]
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
            hc = abs(highs[i] - closes[i-1])
            lc = abs(lows[i] - closes[i-1])
            tr = max(hl, hc, lc)
            tr_values.append(tr)
        if len(tr_values) < period:
            return statistics.mean(tr_values) if tr_values else 0.0
        return self._ema(tr_values, period)

    def _stoch(self, highs: list, lows: list, closes: list,
               k_period: int, d_period: int):
        """Calculate Stochastic Oscillator (%K, %D)."""
        if (len(highs) < k_period or len(lows) < k_period or
                len(closes) < k_period):
            return [0.0, 0.0]

        # Calculate %K values
        k_values = []
        for i in range(k_period - 1, len(closes)):
            high_win = highs[i - k_period + 1:i + 1]
            low_win = lows[i - k_period + 1:i + 1]
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
