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

from pathlib import Path

from pynescript.ast.helper import parse
from pynescript.ast.helper import unparse


def test_parse_and_unparse(pinescript_filepath: Path):
    with open(pinescript_filepath, encoding="utf-8") as f:
        source = f.read()
    parsed_ast = parse(source)
    unparsed_source = unparse(parsed_ast)
    reparsed_ast = parse(unparsed_source)
    assert repr(parsed_ast) == repr(reparsed_ast)
