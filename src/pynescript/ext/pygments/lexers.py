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

from typing import ClassVar

from antlr4 import InputStream
from antlr4 import Token as ANTLR4Token
from pygments.lexer import Lexer
from pygments.token import Token

from pynescript.ast.grammar.antlr4.lexer import PinescriptLexer as PinescriptANTLR4Lexer


class PinescriptLexer(Lexer):
    name: ClassVar[str] = "Pinescript Lexer"

    aliases: ClassVar[list[str]] = ["pinescript"]
    filenames: ClassVar[list[str]] = ["*.pine"]

    url: ClassVar[str] = "https://www.tradingview.com/pine-script-docs/en/v5/Introduction.html"

    _token_type_mapping: ClassVar[dict] = {
        PinescriptANTLR4Lexer.AND: Token.Operator,
        PinescriptANTLR4Lexer.AS: Token.Keyword,
        PinescriptANTLR4Lexer.BREAK: Token.Keyword,
        PinescriptANTLR4Lexer.BY: Token.Keyword,
        PinescriptANTLR4Lexer.CONST: Token.Keyword,
        PinescriptANTLR4Lexer.CONTINUE: Token.Keyword,
        PinescriptANTLR4Lexer.ELSE: Token.Keyword,
        PinescriptANTLR4Lexer.EXPORT: Token.Keyword,
        PinescriptANTLR4Lexer.FALSE: Token.Literal,
        PinescriptANTLR4Lexer.FOR: Token.Keyword,
        PinescriptANTLR4Lexer.IF: Token.Keyword,
        PinescriptANTLR4Lexer.IMPORT: Token.Keyword,
        PinescriptANTLR4Lexer.IN: Token.Keyword,
        PinescriptANTLR4Lexer.INPUT: Token.Keyword,
        PinescriptANTLR4Lexer.METHOD: Token.Keyword,
        PinescriptANTLR4Lexer.NOT: Token.Operator,
        PinescriptANTLR4Lexer.OR: Token.Operator,
        PinescriptANTLR4Lexer.SERIES: Token.Keyword,
        PinescriptANTLR4Lexer.SIMPLE: Token.Keyword,
        PinescriptANTLR4Lexer.SWITCH: Token.Keyword,
        PinescriptANTLR4Lexer.TO: Token.Keyword,
        PinescriptANTLR4Lexer.TYPE: Token.Keyword,
        PinescriptANTLR4Lexer.TRUE: Token.Literal,
        PinescriptANTLR4Lexer.VAR: Token.Keyword,
        PinescriptANTLR4Lexer.VARIP: Token.Keyword,
        PinescriptANTLR4Lexer.WHILE: Token.Keyword,
        PinescriptANTLR4Lexer.WS: Token.Text.Whitespace,
        PinescriptANTLR4Lexer.COMMENT: Token.Comment,
        PinescriptANTLR4Lexer.LPAR: Token.Punctuation,
        PinescriptANTLR4Lexer.RPAR: Token.Punctuation,
        PinescriptANTLR4Lexer.LSQB: Token.Punctuation,
        PinescriptANTLR4Lexer.RSQB: Token.Punctuation,
        PinescriptANTLR4Lexer.LESS: Token.Operator,
        PinescriptANTLR4Lexer.GREATER: Token.Operator,
        PinescriptANTLR4Lexer.EQUAL: Token.Operator,
        PinescriptANTLR4Lexer.EQEQUAL: Token.Operator,
        PinescriptANTLR4Lexer.NOTEQUAL: Token.Operator,
        PinescriptANTLR4Lexer.LESSEQUAL: Token.Operator,
        PinescriptANTLR4Lexer.GREATEREQUAL: Token.Operator,
        PinescriptANTLR4Lexer.RARROW: Token.Punctuation,
        PinescriptANTLR4Lexer.DOT: Token.Punctuation,
        PinescriptANTLR4Lexer.COMMA: Token.Punctuation,
        PinescriptANTLR4Lexer.COLON: Token.Operator,
        PinescriptANTLR4Lexer.QUESTION: Token.Operator,
        PinescriptANTLR4Lexer.PLUS: Token.Operator,
        PinescriptANTLR4Lexer.MINUS: Token.Operator,
        PinescriptANTLR4Lexer.STAR: Token.Operator,
        PinescriptANTLR4Lexer.SLASH: Token.Operator,
        PinescriptANTLR4Lexer.PERCENT: Token.Operator,
        PinescriptANTLR4Lexer.PLUSEQUAL: Token.Operator,
        PinescriptANTLR4Lexer.MINEQUAL: Token.Operator,
        PinescriptANTLR4Lexer.STAREQUAL: Token.Operator,
        PinescriptANTLR4Lexer.SLASHEQUAL: Token.Operator,
        PinescriptANTLR4Lexer.PERCENTEQUAL: Token.Operator,
        PinescriptANTLR4Lexer.COLONEQUAL: Token.Operator,
        PinescriptANTLR4Lexer.NAME: Token.Name,
        PinescriptANTLR4Lexer.NUMBER: Token.Literal.Number,
        PinescriptANTLR4Lexer.STRING: Token.Literal.String,
        PinescriptANTLR4Lexer.COLOR: Token.Literal,
        PinescriptANTLR4Lexer.NEWLINE: Token.Text.Whitespace,
        PinescriptANTLR4Lexer.WS: Token.Text.Whitespace,
        PinescriptANTLR4Lexer.COMMENT: Token.Comment,
        PinescriptANTLR4Lexer.ERROR_TOKEN: Token.Error,
    }

    def get_tokens_unprocessed(self, text: str):
        stream = InputStream(text)
        lexer = PinescriptANTLR4Lexer(stream)
        while True:
            token = lexer.nextToken()
            if token is None:
                return
            if token.type in {ANTLR4Token.EOF}:
                return
            if token.type in {PinescriptANTLR4Lexer.INDENT, PinescriptANTLR4Lexer.DEDENT}:
                continue
            yield token.start, self._token_type_mapping.get(token.type, Token.Other), token.text
