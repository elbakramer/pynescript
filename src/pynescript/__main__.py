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

import click


@click.group()
@click.version_option()
def cli():
    pass


@cli.command(short_help="Parse pinescript file to AST tree.")
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
def parse_and_dump(filename, encoding, indent, output_file):
    from pynescript.ast import dump
    from pynescript.ast import parse

    with click.open_file(filename, "r", encoding=encoding) as f:
        script_node = parse(f.read(), filename)

    script_node_dump = dump(script_node, indent=indent)

    with click.open_file(output_file, "w", encoding=encoding) as f:
        f.write(script_node_dump)


@cli.command(short_help="Parse pinescript file and unparse back to pinescript.")
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
    "--output-file",
    metavar="PATH",
    type=click.Path(writable=True, allow_dash=True),
    help="Path to output dump file, defaults to standard output.",
    default="-",
)
def parse_and_unparse(filename, encoding, output_file):
    from pynescript.ast import parse
    from pynescript.ast import unparse

    with click.open_file(filename, "r", encoding=encoding) as f:
        script_node = parse(f.read(), filename)

    unparsed_script = unparse(script_node)

    with click.open_file(output_file, "w", encoding=encoding) as f:
        f.write(unparsed_script)


@cli.command(short_help="Download builtin scripts.")
@click.option(
    "--script-dir",
    type=click.Path(exists=False, file_okay=False, writable=True),
    help="Diretory where scripts to be saved (like tests/data/builtin_scripts).",
    required=True,
)
def download_builtin_scripts(script_dir):
    from pynescript.util.pine_facade import download_builtin_scripts as download

    download(script_dir)


if __name__ == "__main__":
    cli(prog_name="pynescript")  # pragma: no cover
