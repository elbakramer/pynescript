#!/usr/bin/env python3
"""
Example demonstrating the PineScript expression evaluator.

This shows how the evaluator can handle various PineScript expressions
including math, string operations, arrays, and technical analysis functions.
"""

from pynescript.ast.helper import literal_eval


def main():
    print("=" * 60)
    print("PineScript Expression Evaluator Demo")
    print("=" * 60)

    # Basic arithmetic
    print("\n--- Basic Arithmetic ---")
    print("1 + 2 * 3 =", literal_eval("1 + 2 * 3"))
    print("(1 + 2) * 3 =", literal_eval("(1 + 2) * 3"))
    print("10 / 3 =", literal_eval("10 / 3"))
    print("10 % 3 =", literal_eval("10 % 3"))

    # Math functions
    print("\n--- Math Functions ---")
    print("math.max(1, 5, 3) =", literal_eval("math.max(1, 5, 3)"))
    print("math.min(1, 5, 3) =", literal_eval("math.min(1, 5, 3)"))
    print("math.abs(-5) =", literal_eval("math.abs(-5)"))
    print("math.sqrt(16) =", literal_eval("math.sqrt(16)"))
    print("math.pow(2, 3) =", literal_eval("math.pow(2, 3)"))
    print("math.round(3.7) =", literal_eval("math.round(3.7)"))
    print("math.floor(3.7) =", literal_eval("math.floor(3.7)"))
    print("math.ceil(3.2) =", literal_eval("math.ceil(3.2)"))

    # String functions
    print("\n--- String Functions ---")
    print('str.length("hello") =', literal_eval('str.length("hello")'))
    print('str.upper("hello") =', literal_eval('str.upper("hello")'))
    print('str.lower("WORLD") =', literal_eval('str.lower("WORLD")'))
    print('str.contains("hello world", "wor") =', 
          literal_eval('str.contains("hello world", "wor")'))
    print('str.startswith("hello", "hel") =', 
          literal_eval('str.startswith("hello", "hel")'))

    # Array operations
    print("\n--- Array Operations ---")
    print("[1, 2, 3, 4, 5] =", literal_eval("[1, 2, 3, 4, 5]"))
    print("[1, 2, 3][1] =", literal_eval("[1, 2, 3][1]"))
    print("array.size([1, 2, 3, 4, 5]) =", 
          literal_eval("array.size([1, 2, 3, 4, 5])"))
    print("array.get([10, 20, 30], 2) =", 
          literal_eval("array.get([10, 20, 30], 2)"))
    print("array.push([1, 2], 3) =", 
          literal_eval("array.push([1, 2], 3)"))
    print("array.pop([1, 2, 3]) =", 
          literal_eval("array.pop([1, 2, 3])"))
    print("array.slice([10, 20, 30, 40], 1, 3) =", 
          literal_eval("array.slice([10, 20, 30, 40], 1, 3)"))

    # Technical Analysis - Moving Averages
    print("\n--- Technical Analysis: Moving Averages ---")
    prices = [100, 102, 101, 103, 105, 104, 106, 108, 107, 110]
    print(f"Price series: {prices}")
    print(f"ta.sma(prices, 5) =", 
          literal_eval(f"ta.sma({prices}, 5)"))
    print(f"ta.ema(prices, 5) =", 
          literal_eval(f"ta.ema({prices}, 5)"))
    print(f"ta.wma(prices, 5) =", 
          literal_eval(f"ta.wma({prices}, 5)"))

    # Technical Analysis - Indicators
    print("\n--- Technical Analysis: Indicators ---")
    print(f"ta.rsi(prices, 9) =", 
          literal_eval(f"ta.rsi({prices}, 9)"))
    print(f"ta.stdev(prices, 5) =", 
          literal_eval(f"ta.stdev({prices}, 5)"))
    bb = literal_eval(f"ta.bb({prices}, 5, 2)")
    print(f"ta.bb(prices, 5, 2) = [middle={bb[0]:.2f}, "
          f"upper={bb[1]:.2f}, lower={bb[2]:.2f}]")

    # Technical Analysis - Range and Change
    print("\n--- Technical Analysis: Range & Change ---")
    print(f"ta.highest(prices, 5) =", 
          literal_eval(f"ta.highest({prices}, 5)"))
    print(f"ta.lowest(prices, 5) =", 
          literal_eval(f"ta.lowest({prices}, 5)"))
    print(f"ta.range(prices, 5) =", 
          literal_eval(f"ta.range({prices}, 5)"))
    print(f"ta.change(prices, 1) =", 
          literal_eval(f"ta.change({prices}, 1)"))

    # New TA Functions
    print("\n--- New Technical Analysis: MACD & ATR ---")
    macd_result = literal_eval(f"ta.macd({prices}, 12, 26, 9)")
    print(f"ta.macd(prices, 12, 26, 9) = [macd={macd_result[0]:.2f}, "
          f"signal={macd_result[1]:.2f}, hist={macd_result[2]:.2f}]")
    highs = [101, 103, 102, 104, 106, 105, 107, 109, 108, 111]
    lows = [98, 100, 99, 101, 103, 102, 104, 106, 105, 108]
    closes = prices
    atr_result = literal_eval(f"ta.atr({highs}, {lows}, {closes}, 14)")
    print(f"ta.atr(highs, lows, closes, 14) = {atr_result:.2f}")

    # Utility functions
    print("\n--- Utility Functions ---")
    print("na() =", literal_eval("na()"))
    print("nz(na(), 10) =", literal_eval("nz(na(), 10)"))
    print("bool(1) =", literal_eval("bool(1)"))
    print("int(3.7) =", literal_eval("int(3.7)"))
    print("float(5) =", literal_eval("float(5)"))

    # Conditional expressions
    print("\n--- Conditional Expressions ---")
    print("true ? 1 : 2 =", literal_eval("true ? 1 : 2"))
    print("false ? 1 : 2 =", literal_eval("false ? 1 : 2"))
    print("5 > 3 ? 'yes' : 'no' =", literal_eval("5 > 3 ? 'yes' : 'no'"))

    # Comparison operations
    print("\n--- Comparisons ---")
    print("5 > 3 =", literal_eval("5 > 3"))
    print("5 < 3 =", literal_eval("5 < 3"))
    print("5 == 5 =", literal_eval("5 == 5"))
    print("5 != 3 =", literal_eval("5 != 3"))

    # Series History Access
    print("\n--- Series History Access ---")
    context = {
        'close': [100, 102, 101, 103, 105, 104, 106, 108, 107, 110],
        'open': [99, 101, 100, 102, 104, 103, 105, 107, 106, 109],
        'high': [101, 103, 102, 104, 106, 105, 107, 109, 108, 111],
        'low': [98, 100, 99, 101, 103, 102, 104, 106, 105, 108],
    }
    print(f"Context series lengths: close={len(context['close'])}, etc.")
    print("close[0] (current) =", literal_eval("close[0]", context))
    print("close[1] (previous) =", literal_eval("close[1]", context))
    print("close[2] =", literal_eval("close[2]", context))
    print("open[0] =", literal_eval("open[0]", context))
    print("high[1] =", literal_eval("high[1]", context))
    print("low[0] - low[1] =", literal_eval("low[0] - low[1]", context))

    print("\n" + "=" * 60)
    print("All evaluations completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
