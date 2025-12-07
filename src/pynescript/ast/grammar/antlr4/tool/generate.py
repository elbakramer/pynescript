# Copyright 2025 Yunseong Hwang
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

import shutil
import subprocess

from pathlib import Path


def main():
    script_directory_path = Path(__file__).parent

    grammar_source_directory_path = script_directory_path / ".." / "resource"
    grammar_output_directory_path = script_directory_path / ".." / "generated"

    grammar_file_encoding = "utf-8"

    generate_grammar_command = [
        "antlr4",
        "-o",
        str(grammar_output_directory_path),
        "-lib",
        str(grammar_source_directory_path),
        "-encoding",
        grammar_file_encoding,
        "-listener",
        "-visitor",
        "-Dlanguage=Python3",
        str(grammar_source_directory_path / "*.g4"),
    ]

    subprocess.check_call(generate_grammar_command)  # noqa: S603

    for filename in grammar_source_directory_path.glob("*.py"):
        shutil.copy(filename, grammar_output_directory_path)


if __name__ == "__main__":
    main()
