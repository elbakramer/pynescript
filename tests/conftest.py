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
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from pytest import Metafunc
    from pytest import Parser


tests_dir = Path(__file__).parent
builtin_scripts_dir = tests_dir / "data" / "builtin_scripts"


def pytest_addoption(parser: Parser):
    parser.addoption("--example-scripts-dir", default=builtin_scripts_dir, type=Path)


def pytest_generate_tests(metafunc: Metafunc):
    if "pinescript_filepath" in metafunc.fixturenames:
        example_scripts_dir: Path = metafunc.config.getoption("--example-scripts-dir")
        pinescript_filepaths = example_scripts_dir.glob("*.pine")
        pinescript_filepaths = list(pinescript_filepaths)
        pinescript_filenames = [path.name for path in pinescript_filepaths]
        metafunc.parametrize(
            argnames="pinescript_filepath",
            argvalues=pinescript_filepaths,
            ids=pinescript_filenames,
        )
