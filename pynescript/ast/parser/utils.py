from __future__ import annotations

import sys
import warnings

from collections import Counter

from contextlib import contextmanager
from functools import lru_cache

from pyparsing import col


def identity(x):
    return x


@lru_cache(maxsize=128)
def calc_char_col(loc, string):
    return col(loc, string)


@lru_cache(maxsize=128)
def calc_width(spaces, tab_width=4):
    counts = Counter(spaces)
    expected_chars = [" ", "\t"]
    unexpected_chars = [c not in expected_chars for c in counts.keys()]
    if unexpected_chars:
        warnings.warn(f"Unexpected characters: {unexpected_chars}")
    width = counts[" "] + counts["\t"] * tab_width
    return width


@lru_cache(maxsize=128)
def calc_width_col(loc, string, tab_width=4):
    char_col = calc_char_col(loc, string)
    indent_spaces = string[(loc - char_col + 1) : loc]
    indent_width = calc_width(indent_spaces, tab_width=tab_width)
    width_col = indent_width + 1
    return width_col


@contextmanager
def recursion_limit(limit):
    old_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(limit)
    try:
        yield old_limit
    finally:
        sys.setrecursionlimit(old_limit)
