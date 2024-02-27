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

import re

from antlr4 import FileStream
from antlr4 import InputStream
from antlr4 import Lexer
from antlr4 import Parser
from antlr4 import Token
from antlr4 import TokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.Recognizer import Recognizer

from pynescript.ast.error import SyntaxError
from pynescript.ast.error import SyntaxErrorDetails


class PinescriptErrorListener(ErrorListener):
    # ruff: noqa: N802

    INSTANCE: PinescriptErrorListener | None = None

    def _getFilenameFrom(self, recognizer: Recognizer) -> str:
        if isinstance(recognizer, Parser):
            input_stream = recognizer._input
            if isinstance(input_stream, TokenStream):
                lexer = input_stream.tokenSource
                recognizer = lexer
            else:
                msg = f"unexpected type of input: {type(input_stream)}"
                raise TypeError(msg)
        if isinstance(recognizer, Lexer):
            input_stream = recognizer._input
            if isinstance(input_stream, FileStream):
                return input_stream.fileName
            elif isinstance(input_stream, InputStream):
                if hasattr(input_stream, "getSourceName"):
                    return input_stream.getSourceName()
                elif hasattr(input_stream, "sourceName"):
                    return input_stream.sourceName
                elif input_stream.name:
                    return input_stream.name
                else:
                    return "<unknown>"
            else:
                msg = f"unexpected type of input: {type(input_stream)}"
                raise TypeError(msg)
        else:
            msg = f"unexpected type of recognizer: {type(recognizer)}"
            raise TypeError(msg)

    _LINE_PATTERN = re.compile(r"(.*?(?:\r\n|\n|\r|$))")

    def _splitLines(self, source: str, maxlines: int | None = None) -> list[str]:
        lines = []
        for lineno, match in enumerate(self._LINE_PATTERN.finditer(source), 1):
            if maxlines is not None and lineno > maxlines:
                break
            lines.append(match[0])
        return lines

    def _getInputTextFrom(self, recognizer: Recognizer, lineno: int | None = None) -> str:
        if isinstance(recognizer, Parser):
            input_stream = recognizer._input
            if isinstance(input_stream, TokenStream):
                lexer = input_stream.tokenSource
                recognizer = lexer
            else:
                msg = f"unexpected type of input: {type(input_stream)}"
                raise TypeError(msg)
        if isinstance(recognizer, Lexer):
            input_stream = recognizer._input
            if isinstance(input_stream, InputStream):
                source = str(input_stream)
                if lineno is not None and lineno > 0:
                    lines = self._splitLines(source, maxlines=lineno)
                    source = lines[lineno - 1]
                return source
            else:
                msg = f"unexpected type of input: {type(input_stream)}"
                raise TypeError(msg)
        else:
            msg = f"unexpected type of recognizer: {type(recognizer)}"
            raise TypeError(msg)

    def syntaxError(  # noqa: PLR0913
        self,
        recognizer: Recognizer,
        offendingSymbol: Token,  # noqa: N803
        line: int,
        column: int,
        msg: str,
        e: Exception | None,
    ):
        filename = self._getFilenameFrom(recognizer)
        lineno = line
        offset = column
        text = self._getInputTextFrom(recognizer, lineno)
        symbol_len = offendingSymbol.stop - offendingSymbol.start + 1
        symbol_nls = offendingSymbol.text.count("\n")
        symbol_nlpos = offendingSymbol.text.rfind("\n")
        end_lineno = offendingSymbol.line + symbol_nls
        end_offset = symbol_len - symbol_nlpos + 1 if symbol_nls > 0 else offendingSymbol.column + symbol_len
        details = SyntaxErrorDetails(
            filename,
            lineno,
            offset,
            text,
            end_lineno,
            end_offset,
        )
        error = SyntaxError(msg, details)

        if isinstance(e, SyntaxError):
            e.details = error.details
            error = e
        else:
            error.__cause__ = e

        raise error


PinescriptErrorListener.INSTANCE = PinescriptErrorListener()


__all__ = [
    "PinescriptErrorListener",
]
