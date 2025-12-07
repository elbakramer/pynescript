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

from io import StringIO
from typing import NamedTuple


class SyntaxErrorDetails(NamedTuple):
    filename: str
    lineno: int
    offset: int
    text: str
    end_lineno: int | None = None
    end_offset: int | None = None


class SyntaxError(Exception):  # noqa: A001
    def __init__(self, message: str, *details):
        self.message = message
        if details:
            if len(details) == 1 and isinstance(details[0], SyntaxErrorDetails):
                self.details = details[0]
            else:
                self.details = SyntaxErrorDetails(*details)

    def __str__(self):
        f = StringIO()
        code = self.details.text.lstrip()
        offset = self.details.offset + len(code) - len(self.details.text)
        f.write(self.message)
        f.write("\n")
        f.write(f'  File "{self.details.filename}", line {self.details.lineno}\n')
        f.write(f"    {code}")
        f.write("    ")
        f.write(" " * offset)
        f.write("^")
        return f.getvalue()


class IndentationError(SyntaxError):  # noqa: A001
    pass


__all__ = [
    "IndentationError",
    "SyntaxError",
    "SyntaxErrorDetails",
]
