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
import re

from collections import deque
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from antlr4 import CommonTokenStream
from antlr4 import FileStream
from antlr4 import InputStream

from pynescript.ast import node as ast
from pynescript.ast.builder import PinescriptASTBuilder
from pynescript.ast.grammar.antlr4.error_listener import PinescriptErrorListener
from pynescript.ast.grammar.antlr4.lexer import PinescriptLexer
from pynescript.ast.grammar.antlr4.parser import PinescriptParser
from pynescript.ast.node import AST
from pynescript.ast.node import Expression
from pynescript.util.itertools import grouper


def _add_annotations(script, statements, comments):
    comments_and_statements = itertools.chain(comments, statements)
    comments_and_statements = sorted(comments_and_statements, key=lambda item: (item.lineno, item.col_offset))

    comments_and_statements = itertools.groupby(comments_and_statements, lambda item: isinstance(item, ast.Comment))
    comments_and_statements = [(k, list(g)) for k, g in comments_and_statements]

    if not comments_and_statements[0][0]:
        comments_and_statements.insert(0, (True, []))

    grouped_annotations_and_statements = [
        [c for c in group if c.kind.startswith("@")] if comment else group[0]
        for comment, group in comments_and_statements
    ]

    annotations = [c.value for c in grouped_annotations_and_statements[0] if c.kind.endswith("S")]

    if annotations:
        script.annotations = annotations

    grouped_annotations_and_statement_pairs = grouper(grouped_annotations_and_statements, n=2, incomplete="ignore")

    for comments, statement in grouped_annotations_and_statement_pairs:
        if isinstance(statement, ast.FunctionDef):
            annotations = [c.value for c in comments if c.kind.endswith("F")]
            if annotations:
                statement.annotations = annotations
        elif isinstance(statement, ast.TypeDef):
            annotations = [c.value for c in comments if c.kind.endswith("T")]
            if annotations:
                statement.annotations = annotations
        elif isinstance(statement, ast.Assign):
            annotations = [c.value for c in comments if c.kind.endswith("V")]
            if annotations:
                statement.annotations = annotations


def _parse(
    stream: InputStream,
    mode: str = "exec",
) -> AST:
    if mode not in {"exec", "eval"}:
        msg = f"invalid argument mode: {mode}"
        raise ValueError(msg)

    lexer = PinescriptLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = PinescriptParser(token_stream)
    error_listener = PinescriptErrorListener.INSTANCE

    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    rule = {
        "exec": parser.start_script,
        "eval": parser.start_expression,
    }[mode]()

    builder = PinescriptASTBuilder()
    node = builder.visit(rule)

    if mode == "exec":
        from pynescript.ast.collector import StatementCollector

        statement_collector = StatementCollector()

        statements = statement_collector.visit(node)
        statements = list(statements)

        if not statements:
            return node

        parser.getTokenStream().channel = PinescriptLexer.COMMENT_CHANNEL
        parser.reset()

        comments = builder.visit(parser.start_comments())

        if not comments:
            return node

        _add_annotations(node, statements, comments)

    return node


def _get_absolute_path(filename: str) -> str:
    if filename in {"<unknown>"}:
        return filename
    filename_path = Path(filename)
    if not filename_path.exists():
        return filename
    filename = str(filename_path.absolute())
    return filename


def _parse_inputstream(
    source: str,
    filename: str = "<unknown>",
    mode: str = "exec",
) -> AST:
    filename = _get_absolute_path(filename)
    stream = InputStream(source)
    stream.name = filename
    return _parse(stream, mode)


def _parse_filestream(
    filename: str,
    encoding: str = "utf-8",
    mode: str = "exec",
) -> AST:
    filename = _get_absolute_path(filename)
    stream = FileStream(filename, encoding=encoding)
    return _parse(stream, mode)


def parse(
    source: str,
    filename: str = "<unknown>",
    mode: str = "exec",
) -> AST:
    return _parse_inputstream(source, filename, mode)


def literal_eval(
    node_or_string: AST | str, context: dict[str, Any] | None = None
):
    if isinstance(node_or_string, str):
        node_or_string = parse(node_or_string.lstrip(" \t"), mode="eval")
    if isinstance(node_or_string, Expression):
        node_or_string = node_or_string.body

    from pynescript.ast.evaluator import NodeLiteralEvaluator

    evaluator = NodeLiteralEvaluator(context)
    return evaluator.visit(node_or_string)


def dump(  # noqa: C901
    node: AST,
    *,
    annotate_fields: bool = True,
    include_attributes: bool = False,
    indent: int | None = None,
) -> str:
    def _format(node, level=0):  # noqa: C901, PLR0912
        if indent is not None:
            level += 1
            prefix = "\n" + indent * level
            sep = ",\n" + indent * level
        else:
            prefix = ""
            sep = ", "
        if isinstance(node, AST):
            cls = type(node)
            args = []
            allsimple = True
            keywords = annotate_fields
            for name in node._fields:
                try:
                    value = getattr(node, name)
                except AttributeError:
                    keywords = True
                    continue
                if value is None and getattr(cls, name, ...) is None:
                    keywords = True
                    continue
                value, simple = _format(value, level)
                allsimple = allsimple and simple
                if keywords:
                    args.append(f"{name}={value}")
                else:
                    args.append(value)
            if include_attributes and node._attributes:
                for name in node._attributes:
                    try:
                        value = getattr(node, name)
                    except AttributeError:
                        continue
                    if value is None and getattr(cls, name, ...) is None:
                        continue
                    value, simple = _format(value, level)
                    allsimple = allsimple and simple
                    args.append(f"{name}={value}")
            if allsimple and len(args) <= 3:  # noqa: PLR2004
                return "{}({})".format(node.__class__.__name__, ", ".join(args)), not args
            return f"{node.__class__.__name__}({prefix}{sep.join(args)})", False
        elif isinstance(node, list):
            if not node:
                return "[]", True
            return f"[{prefix}{sep.join(_format(x, level)[0] for x in node)}]", False
        return repr(node), True

    if not isinstance(node, AST):
        raise TypeError("expected AST, got %r" % node.__class__.__name__)

    if indent is not None and not isinstance(indent, str):
        indent = " " * indent

    return _format(node)[0]


def copy_location(new_node: AST, old_node: AST) -> AST:
    for attr in "lineno", "col_offset", "end_lineno", "end_col_offset":
        if attr in old_node._attributes and attr in new_node._attributes:
            value = getattr(old_node, attr, None)
            if value is not None or (hasattr(old_node, attr) and attr.startswith("end_")):
                setattr(new_node, attr, value)
    return new_node


def iter_fields(node: AST) -> Iterator[tuple[str, Any]]:
    for field in node._fields:
        try:
            yield field, getattr(node, field)
        except AttributeError:
            pass


def iter_child_nodes(node: AST) -> Iterator[AST]:
    for _name, field in iter_fields(node):
        if isinstance(field, AST):
            yield field
        elif isinstance(field, list):
            for item in field:
                if isinstance(item, AST):
                    yield item


def _fix_locations(  # noqa: PLR0912
    node: AST,
    lineno: int,
    col_offset: int,
    end_lineno: int,
    end_col_offset: int,
) -> None:
    if "lineno" in node._attributes:
        if not hasattr(node, "lineno"):
            node.lineno = lineno
        else:
            lineno = node.lineno
    if "end_lineno" in node._attributes:
        if getattr(node, "end_lineno", None) is None:
            node.end_lineno = end_lineno
        else:
            end_lineno = node.end_lineno
    if "col_offset" in node._attributes:
        if not hasattr(node, "col_offset"):
            node.col_offset = col_offset
        else:
            col_offset = node.col_offset
    if "end_col_offset" in node._attributes:
        if getattr(node, "end_col_offset", None) is None:
            node.end_col_offset = end_col_offset
        else:
            end_col_offset = node.end_col_offset

    for child in iter_child_nodes(node):
        _fix_locations(child, lineno, col_offset, end_lineno, end_col_offset)


def fix_missing_locations(node: AST) -> AST:
    _fix_locations(node, 1, 0, 1, 0)
    return node


def increment_lineno(node: AST, n: int = 1) -> AST:
    for child in walk(node):
        if "lineno" in child._attributes:
            child.lineno = getattr(child, "lineno", 0) + n
        if "end_lineno" in child._attributes and (end_lineno := getattr(child, "end_lineno", 0)) is not None:
            child.end_lineno = end_lineno + n
    return node


_line_pattern = re.compile(r"(.*?(?:\r\n|\n|\r|$))")


def _splitlines_no_ff(source: str, maxlines: int | None = None) -> list[str]:
    lines = []
    for lineno, match in enumerate(_line_pattern.finditer(source), 1):
        if maxlines is not None and lineno > maxlines:
            break
        lines.append(match[0])
    return lines


def _pad_whitespace(source: str) -> str:
    result = ""
    for c in source:
        if c in "\f\t":
            result += c
        else:
            result += " "
    return result


def get_source_segment(source: str, node: AST, *, padded: bool = False) -> str:
    try:
        if node.end_lineno is None or node.end_col_offset is None:
            return None
        lineno = node.lineno - 1
        end_lineno = node.end_lineno - 1
        col_offset = node.col_offset
        end_col_offset = node.end_col_offset
    except AttributeError:
        return None

    lines = _splitlines_no_ff(source, maxlines=end_lineno + 1)
    if end_lineno == lineno:
        return lines[lineno].encode()[col_offset:end_col_offset].decode()

    if padded:
        padding = _pad_whitespace(lines[lineno].encode()[:col_offset].decode())
    else:
        padding = ""

    first = padding + lines[lineno].encode()[col_offset:].decode()
    last = lines[end_lineno].encode()[:end_col_offset].decode()
    lines = lines[lineno + 1 : end_lineno]

    lines.insert(0, first)
    lines.append(last)
    return "".join(lines)


def walk(node: AST) -> Iterator[AST]:
    todo = deque([node])
    while todo:
        node = todo.popleft()
        todo.extend(iter_child_nodes(node))
        yield node


def unparse(node: AST):
    from pynescript.ast.unparser import NodeUnparser

    unparser = NodeUnparser()
    return unparser.visit(node)


__all__ = [
    "parse",
    "literal_eval",
    "dump",
    "iter_fields",
    "iter_child_nodes",
    "copy_location",
    "fix_missing_locations",
    "increment_lineno",
    "get_source_segment",
    "walk",
    "unparse",
]
