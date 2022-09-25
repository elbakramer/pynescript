import collections
import tempfile

from io import StringIO
from pathlib import Path

import numpy as np
import pandas as pd

from pynescript import ast
from pynescript.ast import NodeTransformer
from pynescript.ast import NodeVisitor
from pynescript.ast import dump
from pynescript.ast import parse
from pynescript.ast import parse_file
from pynescript.ast import parse_string
from pynescript.ast import unparse

SCRIPT = """
//@version=5
strategy("RSI Strategy", overlay=true)
length = input( 14 )
overSold = input( 30 )
overBought = input( 70 )
price = close
vrsi = ta.rsi(price, length)
co = ta.crossover(vrsi, overSold)
cu = ta.crossunder(vrsi, overBought)
if (not na(vrsi))
	if (co)
		strategy.entry("RsiLE", strategy.long, comment="RsiLE")
	if (cu)
		strategy.entry("RsiSE", strategy.short, comment="RsiSE")
//plot(strategy.equity, title="equity", color=color.red, linewidth=2, style=plot.style_areabr)
"""

# parse script string using parse_string()
tree = parse_string(SCRIPT)

# parse script string using parse_file() and StringIO()
tree = parse_file(StringIO(SCRIPT))

# preparing temporary directory for testing reading files
with tempfile.TemporaryDirectory() as temp_dir:
    script_filename = "rsi_strategy.pine"
    script_filepath = Path(temp_dir) / script_filename

    # script written to a file
    with open(script_filepath, "w", encoding="utf-8") as f:
        f.write(SCRIPT)

    # parse script by filename using parse_file()
    tree = parse_file(script_filepath)

    # parse script by open file object using parse_file()
    with open(script_filepath, encoding="utf-8") as f:
        tree = parse_file(f)

    # parse() can do both string and file parsing
    tree = parse(SCRIPT)  # string
    tree = parse(script_filepath)  # filename
    tree = parse(StringIO(SCRIPT))  # file object

# dump tree using dump()
tree_dumped = dump(tree)
print(tree_dumped)

# dump with indent for visibility
tree_dumped = dump(tree, indent=2)
print(tree_dumped)

# unparse parsed tree to generate code
unparsed_script = unparse(tree)
print(unparsed_script)

# can process tree using NodeVisitor() and NodeTransformer()
# implement visit_{NodeType}(node) method to capture node of type {NodeType}

# use NodeVisitor for simple visiting
class PrintFunctionCallsVisitor(NodeVisitor):
    def visit_Call(self, node: ast.Call):
        print(f"called function {node.func} with arguments {node.arguments}")


print_function_calls_visitor = PrintFunctionCallsVisitor()
print_function_calls_visitor.visit(tree)

# use NodeTransformer for transforming values
class SimpleScriptExecutor(NodeTransformer):
    def __init__(self):
        self.cash = 1000
        self.pos_price = 0

        x = np.linspace(0, 2 * np.pi * 5, 1000)
        close = 500 + np.sin(x) * 400 + np.random.rand(1000) * 100
        close = close.tolist()
        close = collections.deque(close)

        self.strategy_once = True

        def strategy(name, /, overlay: bool = False):
            if self.strategy_once:
                print(f"running strategy script `{name}` with overlay = {overlay}")
                self.strategy_once = False

        def input_(default_value: int):
            return default_value

        def rsi(value, length: int):
            end = length * 2
            value = [value[i] for i in range(end)]
            value = list(reversed(value))
            value = pd.Series(value)
            diff = value.diff(1)
            up_direction = diff.where(diff > 0, 0.0)
            down_direction = -diff.where(diff < 0, 0.0)
            emaup = up_direction.ewm(
                alpha=1 / length,
                min_periods=length,
                adjust=False,
            ).mean()
            emadn = down_direction.ewm(
                alpha=1 / length,
                min_periods=length,
                adjust=False,
            ).mean()
            relative_strength = emaup / emadn
            rsi = pd.Series(
                np.where(emadn == 0, 100, 100 - (100 / (1 + relative_strength))),
                index=value.index,
            )
            result = list(reversed(rsi.tolist()))
            return result

        def crossover(value1, value2):
            cur_value1 = value1[0]
            cur_value2 = value2  # [0]
            past_value1 = value1[1]
            past_value2 = value2  # [1]
            return past_value2 > past_value1 and cur_value1 > cur_value2

        def crossunder(value1, value2):
            cur_value1 = value1[0]
            cur_value2 = value2  # [0]
            past_value1 = value1[1]
            past_value2 = value2  # [1]
            return past_value2 < past_value1 and cur_value1 < cur_value2

        def na(value):
            return value is None

        def strategy_entry(label: str, kind, /, comment: str = None):
            price = self.values["close"][0]
            if kind == "long":
                if self.pos_price > 0:
                    print(
                        f"[{label}] tried opening {kind} position "
                        f"at price {price} but skipping due to "
                        f"open {kind} position, comment = {comment}"
                    )
                elif self.pos_price == 0:
                    print(
                        f"[{label}] opening {kind} position "
                        f"at price {price}, comment = {comment}"
                    )
                    self.pos_price = price
                else:
                    gain = price - self.pos_price
                    print(
                        f"[{label}] closing short position "
                        "at price {price} with gain {gain}, "
                        f"comment = {comment}"
                    )
                    self.cash += gain
                    self.pos_price = 0
            else:
                if self.pos_price < 0:
                    print(
                        f"[{label}] tried opening {kind} position "
                        f"at price {price} but skipping due to "
                        f"open {kind} position, comment = {comment}"
                    )
                elif self.pos_price == 0:
                    print(
                        f"[{label}] opening {kind} position "
                        f"at price {price}, comment = {comment}"
                    )
                    self.pos_price = -price
                else:
                    gain = -self.pos_price - price
                    print(
                        f"[{label}] closing long position "
                        f"at price {price} with gain {gain}, "
                        f"comment = {comment}"
                    )
                    self.cash += gain
                    self.pos_price = 0

        self.values = {
            "close": close,
            "strategy": strategy,
            "input": input_,
            "ta.rsi": rsi,
            "ta.crossover": crossover,
            "ta.crossunder": crossunder,
            "na": na,
            "strategy.entry": strategy_entry,
            "strategy.long": "long",
            "strategy.short": "short",
        }

    def get_name(self, node):
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            return f"{self.get_name(node.value)}.{node.attribute}"

    def visit_Name(self, node: ast.Name):
        name = node.id
        return self.values[name]

    def visit_Attribute(self, node: ast.Attribute):
        name = f"{self.get_name(node.value)}.{node.attribute}"
        return self.values[name]

    def visit_Constant(self, node: ast.Constant):
        return node.value

    def visit_Argument(self, node: ast.Argument):
        return self.visit(node.value)

    def visit_Call(self, node: ast.Attribute):
        func = self.visit(node.func)
        arguments = [self.visit(arg) for arg in node.arguments]
        return func(*arguments)

    def visit_Assign(self, node: ast.Assign):
        name = node.target
        value = self.visit(node.value)
        self.values[name] = value
        return value

    def visit_Expr(self, node: ast.Expr):
        return self.visit(node.value)

    def visit_If(self, node: ast.If):
        cond = self.visit(node.condition)
        if cond:
            res = None
            for item in node.body:
                res = self.visit(item)
            return res
        elif node.orelse:
            res = None
            for item in node.orelse:
                res = self.visit(item)
            return res

    def visit_Script(self, node: ast.Script):
        print(f"starting with cash {self.cash}")
        for i in range(1000):
            if i % 10 == 0:
                print(f"running day {i}")
            for stmt in node.body:
                self.visit(stmt)
            self.values["close"].rotate()
        print(f"ended with cash {self.cash}")


simple_script_executor = SimpleScriptExecutor()
simple_script_executor.visit(tree)
