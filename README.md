# Pynescript

[![PyPI](https://img.shields.io/pypi/v/pynescript.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/pynescript.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/pynescript)][python version]
[![License](https://img.shields.io/pypi/l/pynescript)][license]

[![Read the documentation at https://pynescript.readthedocs.io/](https://img.shields.io/readthedocs/pynescript/latest.svg?label=Read%20the%20Docs)][read the docs]

[pypi_]: https://pypi.org/project/pynescript/
[status]: https://pypi.org/project/pynescript/
[python version]: https://pypi.org/project/pynescript
[read the docs]: https://pynescript.readthedocs.io/
[tests]: https://github.com/elbakramer/pynescript/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/elbakramer/pynescript

## Features

Handle [Pinescript] using [Python]

-   Parse Pinescript code into AST
-   Dump parsed AST
-   Unparse parsed AST back to Pinescript code

Given an example pinescript with name of `rsi_strategy.pine`:

```pinescript
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
```

Parsing script into AST and dumping it:

```console
$ pynescript parse-and-dump rsi_strategy.pine
```

Gives like:

```python
Script(
  body=[
    Expr(
      value=Call(
        func=Name(id='strategy', ctx=Load()),
        args=[
          Arg(
            value=Constant(value='RSI Strategy')),
          Arg(
            value=Constant(value=True),
            name='overlay')])),
    Assign(
      target=Name(id='length', ctx=Store()),
      value=Call(
        func=Name(id='input', ctx=Load()),
        args=[
          Arg(
            value=Constant(value=14))]),
      annotations=[]),
    ...
```

<details>
    <summary>Full AST dump that is quite long...</summary>

```python
Script(
  body=[
    Expr(
      value=Call(
        func=Name(id='strategy', ctx=Load()),
        args=[
          Arg(
            value=Constant(value='RSI Strategy')),
          Arg(
            value=Constant(value=True),
            name='overlay')])),
    Assign(
      target=Name(id='length', ctx=Store()),
      value=Call(
        func=Name(id='input', ctx=Load()),
        args=[
          Arg(
            value=Constant(value=14))]),
      annotations=[]),
    Assign(
      target=Name(id='overSold', ctx=Store()),
      value=Call(
        func=Name(id='input', ctx=Load()),
        args=[
          Arg(
            value=Constant(value=30))]),
      annotations=[]),
    Assign(
      target=Name(id='overBought', ctx=Store()),
      value=Call(
        func=Name(id='input', ctx=Load()),
        args=[
          Arg(
            value=Constant(value=70))]),
      annotations=[]),
    Assign(
      target=Name(id='price', ctx=Store()),
      value=Name(id='close', ctx=Load()),
      annotations=[]),
    Assign(
      target=Name(id='vrsi', ctx=Store()),
      value=Call(
        func=Attribute(
          value=Name(id='ta', ctx=Load()),
          attr='rsi',
          ctx=Load()),
        args=[
          Arg(
            value=Name(id='price', ctx=Load())),
          Arg(
            value=Name(id='length', ctx=Load()))]),
      annotations=[]),
    Assign(
      target=Name(id='co', ctx=Store()),
      value=Call(
        func=Attribute(
          value=Name(id='ta', ctx=Load()),
          attr='crossover',
          ctx=Load()),
        args=[
          Arg(
            value=Name(id='vrsi', ctx=Load())),
          Arg(
            value=Name(id='overSold', ctx=Load()))]),
      annotations=[]),
    Assign(
      target=Name(id='cu', ctx=Store()),
      value=Call(
        func=Attribute(
          value=Name(id='ta', ctx=Load()),
          attr='crossunder',
          ctx=Load()),
        args=[
          Arg(
            value=Name(id='vrsi', ctx=Load())),
          Arg(
            value=Name(id='overBought', ctx=Load()))]),
      annotations=[]),
    Expr(
      value=If(
        test=UnaryOp(
          op=Not(),
          operand=Call(
            func=Name(id='na', ctx=Load()),
            args=[
              Arg(
                value=Name(id='vrsi', ctx=Load()))])),
        body=[
          Expr(
            value=If(
              test=Name(id='co', ctx=Load()),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(id='strategy', ctx=Load()),
                      attr='entry',
                      ctx=Load()),
                    args=[
                      Arg(
                        value=Constant(value='RsiLE')),
                      Arg(
                        value=Attribute(
                          value=Name(id='strategy', ctx=Load()),
                          attr='long',
                          ctx=Load())),
                      Arg(
                        value=Constant(value='RsiLE'),
                        name='comment')]))],
              orelse=[])),
          Expr(
            value=If(
              test=Name(id='cu', ctx=Load()),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(id='strategy', ctx=Load()),
                      attr='entry',
                      ctx=Load()),
                    args=[
                      Arg(
                        value=Constant(value='RsiSE')),
                      Arg(
                        value=Attribute(
                          value=Name(id='strategy', ctx=Load()),
                          attr='short',
                          ctx=Load())),
                      Arg(
                        value=Constant(value='RsiSE'),
                        name='comment')]))],
              orelse=[]))],
        orelse=[]))],
  annotations=[
    '//@version=5'])
```

</details>

Parsing into AST and unparsing it back:

```console
$ pynescript parse-and-unparse rsi_strategy.pine
```

Gives (with some difference in syntax including spacing):

```pinescript
//@version=5
strategy("RSI Strategy", overlay=true)
length = input(14)
overSold = input(30)
overBought = input(70)
price = close
vrsi = ta.rsi(price, length)
co = ta.crossover(vrsi, overSold)
cu = ta.crossunder(vrsi, overBought)
if not na(vrsi)
    if co
        strategy.entry("RsiLE", strategy.long, comment="RsiLE")
    if cu
        strategy.entry("RsiSE", strategy.short, comment="RsiSE")
```

## Requirements

-   Python 3.10 or higher

## Installation

You can install _Pynescript_ via [pip] from [PyPI]:

```console
$ pip install pynescript
```

## Usage

Please see the [Usage][usage] for details.

## License

Distributed under the terms of the [LGPL 3.0 license][license],
_Pynescript_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

[pinescript]: https://www.tradingview.com/pine-script-docs/en/v5/Introduction.html
[python]: https://www.python.org/

[pip]: https://pip.pypa.io/
[pypi]: https://pypi.org/

[file an issue]: https://github.com/elbakramer/pynescript/issues

<!-- github-only -->

[license]: https://github.com/elbakramer/pynescript/blob/main/LICENSE
[usage]: https://pynescript.readthedocs.io/en/latest/usage.html
