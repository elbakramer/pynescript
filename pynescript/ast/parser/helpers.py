import re

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
from pynescript.ast.parser.grammars import script, version_comment
from pynescript.ast.parser.utils import recursion_limit as recursion_limit_context


def parse_string(
    code: str,
    parse_all: bool = True,
    expand_tabs: bool = True,
    debug: bool = False,
    tab_width: int = 4,
    recursion_limit: int = 5000,
) -> AST:
    script_expr = script
    version_comment_expr = version_comment

    script_node = None
    script_version = None

    script_expr.parse_with_tabs()
    version_comment_expr.parse_with_tabs()

    if expand_tabs:
        code = code.expandtabs(tab_width)

    version_results = version_comment_expr.search_string(code)

    if version_results:
        script_version = version_results.get("version")

    if debug:
        code_expanded = code.expandtabs(tab_width)
        code_formatted_for_debug = pyparsing.testing.with_line_numbers(code_expanded)
        code_lines_formatted_for_debug = code_formatted_for_debug.split("\n")

        actual_code_start_line_index = 0
        actual_code_start_column_index = 0

        for i in range(len(code_formatted_for_debug)):
            line = code_lines_formatted_for_debug[i]

            if line.lstrip().startswith("1:"):
                actual_code_start_line_index = i
                actual_code_start_column_index = len(line.split(":", 1)[0]) + 1
                break

    try:
        with recursion_limit_context(recursion_limit):
            parse_result = script_expr.parse_string(code, parse_all=parse_all)

    except ParseException as err:
        if debug:
            print()
            print("Error while parsing code:")

            for i, line in enumerate(code_lines_formatted_for_debug):
                lineno = i - actual_code_start_line_index + 1

                if lineno != err.lineno:
                    print(line)
                    continue

                code_line_prefix = line.split(":", 1)[0] + ":"
                err_line = err.line

                print(f"{code_line_prefix}{err_line}")

                code_indent = code[(err.loc - err.col + 1) : err.loc]
                code_indent = re.sub("[^\t]", " ", code_indent)

                arrow_indent = " " * actual_code_start_column_index + code_indent
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
    tab_width: int = 4,
    debug: bool = False,
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
            tab_width=tab_width,
            debug=debug,
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
@click.option(
    "--enable-warnings",
    is_flag=True,
)
def parse_command(filename, encoding, indent, output_file, enable_warnings):
    from pynescript.ast.helpers import dump

    if enable_warnings:
        pyparsing.enable_all_warnings()

    with click.open_file(filename, "r", encoding=encoding) as f:
        script_node = parse(f, encoding=encoding)

    script_node_dump = dump(script_node, indent=indent)

    with click.open_file(output_file, "w", encoding=encoding) as f:
        f.write(script_node_dump)


if __name__ == "__main__":
    cli()
