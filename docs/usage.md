# Usage

## Library

Simple parse, dump, unparse:

```{literalinclude} ../examples/parse_dump_unparse.py
---
language: python
---
```

Traversing parsed AST nodes:

```{note}
Note that this script does not produce a working Python program; it only generates structurally similar code using Python syntax.
```

```{literalinclude} ../examples/convert_to_python.py
---
language: python
---
```

## Cli

```{eval-rst}
.. click:: pynescript.__main__:cli
  :prog: pynescript
  :nested: full
```
