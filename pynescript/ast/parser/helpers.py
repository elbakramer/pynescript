from io import IOBase, RawIOBase, TextIOBase, BytesIO, TextIOWrapper
from os import PathLike
from pathlib import Path
from contextlib import ExitStack
from typing import Union, Optional

import click
import pyparsing

from pyparsing.exceptions import ParseException

from pynescript import ast
from pynescript.ast.types import AST
from pynescript.ast.parser.grammars import version_comment, comment_suppressed, script
from pynescript.ast.parser.utils import (
    calc_width,
    recursion_limit as recursion_limit_context,
)


def parse_string(
    code: str,
    parse_all: bool = True,
    expand_tabs: bool = True,
    debug: bool = False,
    tab_width: int = 4,
    recursion_limit: int = 1000,
) -> AST:
    version_comment_expr = version_comment.copy()
    comment_suppressed_expr = comment_suppressed.copy()
    script_expr = script.copy()

    version_comment_expr = version_comment_expr.parse_with_tabs()
    comment_suppressed_expr = comment_suppressed_expr.parse_with_tabs()
    script_expr = script_expr.parse_with_tabs()

    script_node = None
    script_version = None

    if expand_tabs:
        code = code.expandtabs(tab_width)

    version_results = version_comment_expr.search_string(code)

    if version_results:
        version_result = version_results[0]
        script_version = version_result.get("version")

    code_without_comment = comment_suppressed_expr.transform_string(code, debug=False)

    if debug:
        code_expanded = code.expandtabs(tab_width)
        code_formatted_for_debug = pyparsing.testing.with_line_numbers(code_expanded)

        code_lines = code.split("\n")
        code_lines_formatted_for_debug = code_formatted_for_debug.split("\n")

        actual_code_start_line_index = 0
        actual_code_start_column_index = 0

        for i in range(len(code_formatted_for_debug)):
            line = code_lines_formatted_for_debug[i]

            if line.lstrip().startswith("1:"):
                actual_code_start_line_index = i
                actual_code_start_column_index = len(line.split(":", 1)[0]) + 1
                break

        indent_from_formatting = " " * actual_code_start_column_index

    try:
        with recursion_limit_context(recursion_limit):
            parse_result = script_expr.parse_string(
                code_without_comment, parse_all=parse_all
            )

    except ParseException as err:
        if debug:
            print()
            print("Error while parsing code:")

            for i, formatted_line in enumerate(code_lines_formatted_for_debug):
                print(formatted_line)

                lineno = i - actual_code_start_line_index + 1

                if err.lineno != lineno:
                    continue

                code_line = code_lines[err.lineno - 1]
                code_line_until_col = code_line[: (err.col - 1)]
                indent_until_col = calc_width(code_line_until_col, tab_width=tab_width)

                arrow_indent = indent_from_formatting + indent_until_col
                arrow = "^"

                print(f"{arrow_indent}{arrow}")
                print(f"{arrow_indent}{err}")

        raise err

    if parse_result:
        script_node = parse_result[0]
    else:
        script_node = ast.Script([])

    if script_version is not None:
        script_node.version = script_version

    return script_node


def parse(
    f: Union[str, PathLike, bytes, IOBase],
    encoding: Optional[str] = None,
    parse_all: bool = True,
    expand_tabs: bool = True,
    debug: bool = False,
    tab_width: int = 4,
    recursion_limit: int = 1000,
) -> AST:
    if encoding is None:
        encoding = "utf-8"

    with ExitStack() as stack:
        code = None

        if isinstance(f, str):
            filename = Path(f)
            if filename.exists():
                f = filename
            else:
                code = f
        if isinstance(f, Path):
            f = stack.enter_context(open(f, encoding=encoding))
        if isinstance(f, bytes):
            f = BytesIO(f)
        if isinstance(f, RawIOBase):
            f = TextIOWrapper(f, encoding=encoding)
        if isinstance(f, TextIOBase):
            code = f.read()

        if code is None:
            raise TypeError(f"Unsupported argument type: {type(f)}")

        script_node = parse_string(
            code,
            parse_all=parse_all,
            expand_tabs=expand_tabs,
            debug=debug,
            tab_width=tab_width,
            recursion_limit=recursion_limit,
        )

        return script_node


@click.group()
def cli():
    pass


@cli.command("parse", short_help="Parse pinescript file.")
@click.argument(
    "filename",
    metavar="PATH",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True),
)
@click.option(
    "--encoding",
    default="utf-8",
    help="Text encoding of the file.",
)
@click.option(
    "--indent",
    type=int,
    default=2,
    help="Indentation with of an AST dump.",
)
@click.option(
    "--output-file",
    metavar="PATH",
    type=click.Path(writable=True, allow_dash=True),
    help="Path to output dump file, defaults to standard output.",
    default="-",
)
def parse_command(filename, encoding, indent, output_file):
    from pynescript.ast.helpers import dump

    with click.open_file(filename, "r", encoding=encoding) as f:
        script_node = parse(f, encoding=encoding)

    script_node_dump = dump(script_node, indent=indent)

    with click.open_file(output_file, "w", encoding=encoding) as f:
        f.write(script_node_dump)


if __name__ == "__main__":
    cli()
