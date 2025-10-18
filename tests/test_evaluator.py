from __future__ import annotations

import math

import pytest

from pynescript.ast import helper
from pynescript.ast.evaluator import NodeLiteralEvaluator


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("abs(-1)", 1),
        ("abs(1)", 1),
        ("abs(0)", 0),
        ("abs(-1.5)", 1.5),
        ("abs(1.5)", 1.5),
    ],
)
def test_evaluator_abs(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.max(1, 2, 3)", 3),
        ("math.max(-1, -2, -3)", -1),
        ("math.max(1.5, 2.5, 3.5)", 3.5),
    ],
)
def test_evaluator_math_max(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.min(1, 2, 3)", 1),
        ("math.min(-1, -2, -3)", -3),
        ("math.min(1.5, 2.5, 3.5)", 1.5),
    ],
)
def test_evaluator_math_min(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.sqrt(4)", 2),
        ("math.sqrt(2)", 1.4142135623730951),
        ("math.sqrt(0)", 0),
    ],
)
def test_evaluator_math_sqrt(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.round(1.5)", 2),
        ("math.round(1.4)", 1),
        ("math.round(1.55, 1)", 1.6),
    ],
)
def test_evaluator_math_round(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.floor(1.9)", 1),
        ("math.floor(-1.9)", -2),
    ],
)
def test_evaluator_math_floor(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.ceil(1.1)", 2),
        ("math.ceil(-1.9)", -1),
    ],
)
def test_evaluator_math_ceil(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.pow(2, 3)", 8),
        ("math.pow(4, 0.5)", 2),
    ],
)
def test_evaluator_math_pow(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.log(100, 10)", 2),
        (f"math.log({math.e})", 1),
    ],
)
def test_evaluator_math_log(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.sin(0)", 0),
        (f"math.sin({math.pi / 2})", 1),
    ],
)
def test_evaluator_math_sin(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.cos(0)", 1),
        (f"math.cos({math.pi})", -1),
    ],
)
def test_evaluator_math_cos(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.tan(0)", 0),
        (f"math.tan({math.pi / 4})", 1),
    ],
)
def test_evaluator_math_tan(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.acos(1)", 0),
        ("math.acos(0)", math.pi / 2),
    ],
)
def test_evaluator_math_acos(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.asin(0)", 0),
        ("math.asin(1)", math.pi / 2),
    ],
)
def test_evaluator_math_asin(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.atan(0)", 0),
        ("math.atan(1)", math.pi / 4),
    ],
)
def test_evaluator_math_atan(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.exp(0)", 1),
        ("math.exp(1)", math.e),
    ],
)
def test_evaluator_math_exp(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.log10(100)", 2),
        ("math.log10(1)", 0),
    ],
)
def test_evaluator_math_log10(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.sign(10)", 1),
        ("math.sign(-10)", -1),
        ("math.sign(0)", 0),
    ],
)
def test_evaluator_math_sign(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.sum([1, 2, 3])", 6),
        ("math.sum([-1, 1, 0])", 0),
    ],
)
def test_evaluator_math_sum(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.avg([1, 2, 3])", 2),
        ("math.avg([10, 20, 30])", 20),
    ],
)
def test_evaluator_math_avg(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.todegrees(math.pi)", 180),
        ("math.todegrees(0)", 0),
    ],
)
def test_evaluator_math_todegrees(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("math.toradians(180)", math.pi),
        ("math.toradians(0)", 0),
    ],
)
def test_evaluator_math_toradians(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert pytest.approx(result) == expected


def test_evaluator_enum_def():
    script = """
enum CalcType
    hl
    hlc
"""
    ast = helper.parse(script)
    evaluator = NodeLiteralEvaluator()
    evaluator.visit(ast)

    expected_context = {
        "CalcType": {
            "hl": "CalcType.hl",
            "hlc": "CalcType.hlc",
        }
    }
    assert evaluator.context["CalcType"] == expected_context["CalcType"]


def test_evaluator_enum_member_access():
    script = """
enum CalcType
    hl
    hlc
a = CalcType.hl
"""
    ast = helper.parse(script)
    evaluator = NodeLiteralEvaluator()
    evaluator.visit(ast)

    assert evaluator.context.get("a") == "CalcType.hl"


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.length("hello")', 5),
        ('str.length("")', 0),
    ],
)
def test_evaluator_str_length(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.upper("hello")', "HELLO"),
        ('str.upper("WORLD")', "WORLD"),
    ],
)
def test_evaluator_str_upper(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.lower("HELLO")', "hello"),
        ('str.lower("world")', "world"),
    ],
)
def test_evaluator_str_lower(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.contains("hello world", "world")', True),
        ('str.contains("hello world", "foo")', False),
    ],
)
def test_evaluator_str_contains(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.startswith("hello world", "hello")', True),
        ('str.startswith("hello world", "world")', False),
    ],
)
def test_evaluator_str_startswith(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.endswith("hello world", "world")', True),
        ('str.endswith("hello world", "hello")', False),
    ],
)
def test_evaluator_str_endswith(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.substring("hello", 1)', "ello"),
        ('str.substring("hello", 1, 3)', "el"),
    ],
)
def test_evaluator_str_substring(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.repeat("a", 5)', "aaaaa"),
        ('str.repeat("ab", 3)', "ababab"),
    ],
)
def test_evaluator_str_repeat(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.replace("hello world", "world", "pine")', "hello pine"),
        ('str.replace("abab", "a", "c")', "cbab"),
    ],
)
def test_evaluator_str_replace(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.replace_all("abab", "a", "c")', "cbcb"),
    ],
)
def test_evaluator_str_replace_all(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.split("a,b,c", ",")', ["a", "b", "c"]),
        ('str.split("a b c")', ["a", "b", "c"]),
    ],
)
def test_evaluator_str_split(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.trim("  hello  ")', "hello"),
    ],
)
def test_evaluator_str_trim(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('str.tonumber("123.45")', 123.45),
    ],
)
def test_evaluator_str_tonumber(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("str.tostring(123)", "123"),
        ('str.tostring("abc")', "abc"),
    ],
)
def test_evaluator_str_tostring(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.size([1, 2, 3])", 3),
        ("array.size([])", 0),
    ],
)
def test_evaluator_array_size(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.get([1, 2, 3], 1)", 2),
    ],
)
def test_evaluator_array_get(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.push([1, 2], 3)", [1, 2, 3]),
    ],
)
def test_evaluator_array_push(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.pop([1, 2, 3])", [1, 2]),
        ("array.pop(array.pop([1]))", []),
    ],
)
def test_evaluator_array_pop(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.slice([1, 2, 3, 4], 1, 3)", [2, 3]),
    ],
)
def test_evaluator_array_slice(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.abs([-1, -2, 3])", [1, 2, 3]),
    ],
)
def test_evaluator_array_abs(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.avg([1, 2, 3])", 2),
    ],
)
def test_evaluator_array_avg(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.concat([1, 2], [3, 4])", [1, 2, 3, 4]),
    ],
)
def test_evaluator_array_concat(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.copy([1, 2, 3])", [1, 2, 3]),
    ],
)
def test_evaluator_array_copy(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.fill([1, 2, 3], 0)", [0, 0, 0]),
    ],
)
def test_evaluator_array_fill(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.first([1, 2, 3])", 1),
    ],
)
def test_evaluator_array_first(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.from(1, 2, 3)", [1, 2, 3]),
    ],
)
def test_evaluator_array_from(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.includes([1, 2, 3], 2)", True),
        ("array.includes([1, 2, 3], 4)", False),
    ],
)
def test_evaluator_array_includes(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.indexof([1, 2, 3], 2)", 1),
        ("array.indexof([1, 2, 3], 4)", -1),
    ],
)
def test_evaluator_array_indexof(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.insert([1, 3], 1, 2)", [1, 2, 3]),
    ],
)
def test_evaluator_array_insert(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ('array.join([1, 2, 3], ",")', "1,2,3"),
    ],
)
def test_evaluator_array_join(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.last([1, 2, 3])", 3),
    ],
)
def test_evaluator_array_last(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.lastindexof([1, 2, 3, 2], 2)", 3),
        ("array.lastindexof([1, 2, 3], 4)", -1),
    ],
)
def test_evaluator_array_lastindexof(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.max([1, 3, 2])", 3),
    ],
)
def test_evaluator_array_max(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.min([2, 1, 3])", 1),
    ],
)
def test_evaluator_array_min(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.range(1, 5)", [1, 2, 3, 4, 5]),
    ],
)
def test_evaluator_array_range(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.remove([1, 2, 3], 1)", [1, 3]),
    ],
)
def test_evaluator_array_remove(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.reverse([1, 2, 3])", [3, 2, 1]),
    ],
)
def test_evaluator_array_reverse(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.set([1, 2, 3], 1, 4)", [1, 4, 3]),
    ],
)
def test_evaluator_array_set(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.shift([1, 2, 3])", [2, 3]),
    ],
)
def test_evaluator_array_shift(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.sort([3, 1, 2])", [1, 2, 3]),
    ],
)
def test_evaluator_array_sort(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.sum([1, 2, 3])", 6),
    ],
)
def test_evaluator_array_sum(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("array.unshift([2, 3], 1)", [1, 2, 3]),
    ],
)
def test_evaluator_array_unshift(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("ta.sma([1, 2, 3, 4, 5], 3)", [None, None, 2, 3, 4]),
    ],
)
def test_evaluator_ta_sma(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == expected


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        (
            "ta.ema([1, 2, 3, 4, 5], 3)",
            [1, 1.5, 2.25, 3.125, 4.0625],
        ),
    ],
)
def test_evaluator_ta_ema(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        (
            (
                "ta.rsi([44.34, 44.09, 44.15, 43.61, 44.33, 44.83, 45.10, 45.42, "
                "45.84, 46.08, 45.89, 46.03, 45.61, 46.28, 46.28], 14)"
            ),
            [
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, 53.3138, 53.3138
            ],
        ),
    ],
)
def test_evaluator_ta_rsi(expression, expected):
    ast = helper.parse(expression, mode="eval")
    evaluator = NodeLiteralEvaluator()
    result = evaluator.visit(ast.body)
    assert result == pytest.approx(expected, abs=1e-4)
