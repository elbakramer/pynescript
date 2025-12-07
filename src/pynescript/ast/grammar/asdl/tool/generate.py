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
import sys

from pathlib import Path


def main():
    script_directory_path = Path(__file__).parent

    asdl_generate_script_path = script_directory_path / "asdlgen.py"

    asdl_source_directory_path = script_directory_path / ".." / "resource"
    asdl_source_path = asdl_source_directory_path / "Pinescript.asdl"
    asdl_output_directory_path = script_directory_path / ".." / "generated"
    asdl_output_path = asdl_output_directory_path / "PinescriptASTNode.py"

    generate_ast_nodes_command = [
        sys.executable,
        str(asdl_generate_script_path),
        str(asdl_source_path),
        "-o",
        str(asdl_output_path),
    ]

    subprocess.check_call(generate_ast_nodes_command)  # noqa: S603

    ruff = shutil.which("ruff")

    if ruff:
        format_ast_nodes_command = [
            ruff,
            "format",
            "--silent",
            str(asdl_output_path),
        ]

        subprocess.call(format_ast_nodes_command)  # noqa: S603

    for filename in asdl_source_directory_path.glob("*.py"):
        shutil.copy(filename, asdl_output_directory_path)


if __name__ == "__main__":
    main()
