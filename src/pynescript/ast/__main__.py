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

from pynescript.ast.helper import dump
from pynescript.ast.helper import parse


def main():
    import argparse

    parser = argparse.ArgumentParser(prog="python -m pynescript.ast")
    parser.add_argument(
        "infile",
        type=argparse.FileType(mode="rb"),
        nargs="?",
        default="-",
        help="the file to parse; defaults to stdin",
    )
    parser.add_argument(
        "-m",
        "--mode",
        default="exec",
        choices=("exec", "eval"),
        help="specify what kind of code must be parsed",
    )
    parser.add_argument(
        "--no-type-comments",
        default=True,
        action="store_false",
        help="don't add information about type comments",
    )
    parser.add_argument(
        "-a",
        "--include-attributes",
        action="store_true",
        help="include attributes such as line numbers and column offsets",
    )
    parser.add_argument("-i", "--indent", type=int, default=2, help="indentation of nodes (number of spaces)")
    args = parser.parse_args()

    with args.infile as infile:
        source = infile.read()

    tree = parse(source, args.infile.name, args.mode)
    print(dump(tree, include_attributes=args.include_attributes, indent=args.indent))  # noqa:T201


if __name__ == "__main__":
    main()
