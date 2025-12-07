# SPDX-FileCopyrightText: 2025 Yunseong Hwang
# SPDX-License-Identifier: LGPL-3.0-or-later

from __future__ import annotations

from pynescript.ast import dump
from pynescript.ast import parse
from pynescript.ast import unparse


script_source = """
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

tree = parse(script_source)
tree_dump = dump(tree, indent=2)
tree_unparsed = unparse(tree)

print("DUMP:")
print(tree_dump)
print()

print("UNPARSED:")
print(tree_unparsed)
print()
