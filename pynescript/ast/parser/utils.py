from __future__ import annotations

import sys
import unicodedata

from collections import Counter

from contextlib import contextmanager
from functools import lru_cache

from pyparsing import col


def identity(x):
    return x


@lru_cache(maxsize=128)
def calc_char_col(loc, string):
    return col(loc, string)


unicodedata_width_mapping = {
    "A": 2,
    "F": 2,
    "H": 1,
    "N": 1,
    "Na": 1,
    "W": 2,
}


@lru_cache(maxsize=128)
def calc_width(chars, tab_width=4):
    counts = Counter(chars)
    width = 0
    for char, count in counts.items():
        if char == "\t":
            char_width = tab_width
        else:
            char_width = unicodedata.east_asian_width(char)
            char_width = unicodedata_width_mapping.get(char_width, 1)
        width += char_width * count
    return width


@lru_cache(maxsize=128)
def calc_width_col(loc, string, tab_width=4):
    char_col = calc_char_col(loc, string)
    indent_chars = string[(loc - char_col + 1) : loc]
    indent_width = calc_width(indent_chars, tab_width=tab_width)
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
