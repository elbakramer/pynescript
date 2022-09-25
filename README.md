# Pynescript

[![PyPI](https://img.shields.io/pypi/v/pynescript.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/pynescript.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/pynescript)][python version]
[![License](https://img.shields.io/pypi/l/pynescript)][license]

[![Read the documentation at https://pynescript.readthedocs.io/](https://img.shields.io/readthedocs/pynescript/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/elbakramer/pynescript/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/elbakramer/pynescript/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/pynescript/
[status]: https://pypi.org/project/pynescript/
[python version]: https://pypi.org/project/pynescript
[read the docs]: https://pynescript.readthedocs.io/
[tests]: https://github.com/elbakramer/pynescript/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/elbakramer/pynescript
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

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
        func=Name(
          id='strategy',
        ),
        arguments=[
          Argument(
            value=Constant(
              value='RSI Strategy',
            ),
            name=None,
          ),
          Argument(
            value=Constant(
              value=True,
            ),
            name='overlay',
          ),
        ],
        type_argument=None,
      ),
    ),
    Assign(
      target='length',
      value=Call(
        func=Name(
          id='input',
        ),
        arguments=[
          Argument(
            value=Constant(
              value=14,
            ),
            name=None,
          ),
        ],
        type_argument=None,
      ),
      declaration_mode=None,
      type_specifier=None,
    ),
    ...
```

<details>
    <summary>Full AST dump that is quote long...</summary>

```python
Script(
  body=[
    Expr(
      value=Call(
        func=Name(
          id='strategy',
        ),
        arguments=[
          Argument(
            value=Constant(
              value='RSI Strategy',
            ),
            name=None,
          ),
          Argument(
            value=Constant(
              value=True,
            ),
            name='overlay',
          ),
        ],
        type_argument=None,
      ),
    ),
    Assign(
      target='length',
      value=Call(
        func=Name(
          id='input',
        ),
        arguments=[
          Argument(
            value=Constant(
              value=14,
            ),
            name=None,
          ),
        ],
        type_argument=None,
      ),
      declaration_mode=None,
      type_specifier=None,
    ),
    Assign(
      target='overSold',
      value=Call(
        func=Name(
          id='input',
        ),
        arguments=[
          Argument(
            value=Constant(
              value=30,
            ),
            name=None,
          ),
        ],
        type_argument=None,
      ),
      declaration_mode=None,
      type_specifier=None,
    ),
    Assign(
      target='overBought',
      value=Call(
        func=Name(
          id='input',
        ),
        arguments=[
          Argument(
            value=Constant(
              value=70,
            ),
            name=None,
          ),
        ],
        type_argument=None,
      ),
      declaration_mode=None,
      type_specifier=None,
    ),
    Assign(
      target='price',
      value=Name(
        id='close',
      ),
      declaration_mode=None,
      type_specifier=None,
    ),
    Assign(
      target='vrsi',
      value=Call(
        func=Attribute(
          value=Name(
            id='ta',
          ),
          attribute='rsi',
        ),
        arguments=[
          Argument(
            value=Name(
              id='price',
            ),
            name=None,
          ),
          Argument(
            value=Name(
              id='length',
            ),
            name=None,
          ),
        ],
        type_argument=None,
      ),
      declaration_mode=None,
      type_specifier=None,
    ),
    Assign(
      target='co',
      value=Call(
        func=Attribute(
          value=Name(
            id='ta',
          ),
          attribute='crossover',
        ),
        arguments=[
          Argument(
            value=Name(
              id='vrsi',
            ),
            name=None,
          ),
          Argument(
            value=Name(
              id='overSold',
            ),
            name=None,
          ),
        ],
        type_argument=None,
      ),
      declaration_mode=None,
      type_specifier=None,
    ),
    Assign(
      target='cu',
      value=Call(
        func=Attribute(
          value=Name(
            id='ta',
          ),
          attribute='crossunder',
        ),
        arguments=[
          Argument(
            value=Name(
              id='vrsi',
            ),
            name=None,
          ),
          Argument(
            value=Name(
              id='overBought',
            ),
            name=None,
          ),
        ],
        type_argument=None,
      ),
      declaration_mode=None,
      type_specifier=None,
    ),
    Expr(
      value=If(
        condition=Unary(
          operator=Not(),
          operand=Call(
            func=Name(
              id='na',
            ),
            arguments=[
              Argument(
                value=Name(
                  id='vrsi',
                ),
                name=None,
              ),
            ],
            type_argument=None,
          ),
        ),
        body=[
          Expr(
            value=If(
              condition=Name(
                id='co',
              ),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='strategy',
                      ),
                      attribute='entry',
                    ),
                    arguments=[
                      Argument(
                        value=Constant(
                          value='RsiLE',
                        ),
                        name=None,
                      ),
                      Argument(
                        value=Attribute(
                          value=Name(
                            id='strategy',
                          ),
                          attribute='long',
                        ),
                        name=None,
                      ),
                      Argument(
                        value=Constant(
                          value='RsiLE',
                        ),
                        name='comment',
                      ),
                    ],
                    type_argument=None,
                  ),
                ),
              ],
              orelse=None,
            ),
          ),
          Expr(
            value=If(
              condition=Name(
                id='cu',
              ),
              body=[
                Expr(
                  value=Call(
                    func=Attribute(
                      value=Name(
                        id='strategy',
                      ),
                      attribute='entry',
                    ),
                    arguments=[
                      Argument(
                        value=Constant(
                          value='RsiSE',
                        ),
                        name=None,
                      ),
                      Argument(
                        value=Attribute(
                          value=Name(
                            id='strategy',
                          ),
                          attribute='short',
                        ),
                        name=None,
                      ),
                      Argument(
                        value=Constant(
                          value='RsiSE',
                        ),
                        name='comment',
                      ),
                    ],
                    type_argument=None,
                  ),
                ),
              ],
              orelse=None,
            ),
          ),
        ],
        orelse=None,
      ),
    ),
  ],
  version=5,
)
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

## Future Plans

-   [Tradingview]-less standalone local back-testing and live-trading using [NautilusTrader]

## Requirements

-   Python 3.8 or higher

## Installation

You can install _Pynescript_ via [pip] from [PyPI]:

```console
$ pip install pynescript
```

## Usage

Please see the [Usage][usage] for details.

Also check out [example_usage.py][example usage] script for examples.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [LGPL 3.0 license][license],
_Pynescript_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/elbakramer/pynescript/issues
[pip]: https://pip.pypa.io/
[pinescript]: https://www.tradingview.com/pine-script-docs/en/v5/Introduction.html
[python]: https://www.python.org/
[tradingview]: https://tradingview.com/
[nautilustrader]: https://github.com/nautechsystems/nautilus_trader
[example usage]: https://github.com/elbakramer/pynescript/blob/main/example_usage.py

<!-- github-only -->

[license]: https://github.com/elbakramer/pynescript/blob/main/LICENSE
[contributor guide]: https://github.com/elbakramer/pynescript/blob/main/CONTRIBUTING.md
[usage]: https://pynescript.readthedocs.io/en/latest/usage.html
