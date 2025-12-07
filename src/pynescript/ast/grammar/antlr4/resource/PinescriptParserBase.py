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

import sys

from typing import TextIO

from antlr4 import Parser
from antlr4 import TokenStream


class PinescriptParserBase(Parser):
    # ruff: noqa: N802, N803, A002

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)

    def isEqualToCurrentTokenText(self, tokenText: str) -> bool:
        return self.getCurrentToken().text == tokenText

    def isNotEqualToCurrentTokenText(self, tokenText: str) -> bool:
        return not self.isEqualToCurrentTokenText(tokenText)
