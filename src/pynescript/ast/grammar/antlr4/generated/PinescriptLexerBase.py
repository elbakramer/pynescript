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

import re
import sys

from collections import deque
from typing import TYPE_CHECKING
from typing import TextIO

from antlr4 import InputStream
from antlr4 import Lexer
from antlr4 import Token

from pynescript.ast.error import IndentationError  # noqa: A004
from pynescript.ast.error import SyntaxError  # noqa: A004


if TYPE_CHECKING:
    from antlr4.Token import CommonToken


class PinescriptLexerBase(Lexer):
    """
    - ignore possible leading newlines
    - ignore excessive trailing newlines except a single newline
    - ensure that script ends with a newline if none
    - ignore consecutive newlines except the last one
    - ignore newlines inside open parentheses, brackets
    - ignore newlines after operators
    - ignore newlines for line wrapping (lines whose indentation width is not a multiple of four)
    - track indentation level, push INDENT or DEDENT token respectfully
    - handle multiline string literal correctly (ignore <newline + indentation for line wrapping>)
    """

    def __init__(self, input: InputStream, output: TextIO = sys.stdout):
        super().__init__(input, output)

        # operators that are followed by terms
        self._operators = {
            self.AND,
            self.COLON,
            self.COLONEQUAL,
            self.COMMA,
            self.EQEQUAL,
            self.EQUAL,
            self.GREATER,
            self.GREATEREQUAL,
            self.LESS,
            self.LESSEQUAL,
            self.MINEQUAL,
            self.MINUS,
            self.NOTEQUAL,
            self.OR,
            self.PERCENT,
            self.PERCENTEQUAL,
            self.PLUS,
            self.PLUSEQUAL,
            self.QUESTION,
            self.SLASH,
            self.SLASHEQUAL,
            self.STAR,
            self.STAREQUAL,
        }

        # indent specific parameters
        self._tabLength: int = 4
        self._indentLength: int = 4

        # track internal tokens
        self._currentToken: CommonToken | None = None
        self._followingToken: CommonToken | None = None

        # keep pending tokens
        self._pendingTokens: list[CommonToken] = []

        # track last pending token types
        self._lastPendingTokenType: int = 0
        self._lastPendingTokenTypeFromDefaultChannel: int = 0

        # track number of opens
        self._numOpens: int = 0

        # track indentations
        self._indentLengthStack: deque[int] = deque()

    def _resetInternalStates(self):
        self._currentToken: CommonToken | None = None
        self._followingToken: CommonToken | None = None
        self._pendingTokens: list[CommonToken] = []
        self._lastPendingTokenType: int = 0
        self._lastPendingTokenTypeFromDefaultChannel: int = 0
        self._numOpens: int = 0
        self._indentLengthStack = deque()

    def nextToken(self) -> CommonToken:
        self._checkNextToken()
        return self._popPendingToken()

    def _checkNextToken(self) -> None:
        if self._reachedEndOfFile():
            return

        self._setNextInternalTokens()
        self._handleStartOfInputIfNecessary()

        match self._currentToken.type:
            case self.LPAR | self.LSQB:
                self._numOpens += 1
                self._addPendingToken(self._currentToken)
            case self.RPAR | self.RSQB:
                self._numOpens -= 1
                self._addPendingToken(self._currentToken)
            case self.NEWLINE:
                self._handle_NEWLINE_token()
            case self.STRING:
                self._handle_STRING_token()
            case self.ERROR_TOKEN:
                message = "token recognition error at: '" + self._currentToken.text + "'"
                self._reportLexerError(message, self._currentToken, SyntaxError)
                self._addPendingToken(self._currentToken)
            case Token.EOF:
                self._handle_EOF_token()
            case _:
                self._addPendingToken(self._currentToken)

    def _reachedEndOfFile(self) -> bool:
        return self._lastPendingTokenType == Token.EOF

    def _setNextInternalTokens(self) -> None:
        self._currentToken = super().nextToken() if self._followingToken is None else self._followingToken
        self._followingToken = self._currentToken if self._currentToken.type == Token.EOF else super().nextToken()

    def _handleStartOfInputIfNecessary(self):
        if len(self._indentLengthStack) > 0:
            return
        self._indentLengthStack.append(0)
        while self._currentToken.type != Token.EOF:
            if self._currentToken.channel == Token.DEFAULT_CHANNEL:
                if self._currentToken.type == self.NEWLINE:
                    self._hideAndAddPendingToken(self._currentToken)
                else:
                    self._checkLeadingIndentIfAny()
                    return
            else:
                self._addPendingToken(self._currentToken)
            self._setNextInternalTokens()

    def _checkLeadingIndentIfAny(self):
        if self._lastPendingTokenType == self.WS:
            prev_token: CommonToken = self._pendingTokens[-1]
            if self._getIndentationLength(prev_token.text) != 0:
                message = "first statement indented"
                self._reportLexerError(message, self._currentToken, IndentationError)
                self._createAndAddPendingToken(self.INDENT, Token.DEFAULT_CHANNEL, message, self._currentToken)

    def _getIndentationLength(self, text: str) -> int:
        length = 0
        for ch in text:
            match ch:
                case " ":
                    length += 1
                case "\t":
                    length += self._tabLength
                case "\f":
                    length = 0
        return length

    def _createAndAddPendingToken(self, type: int, channel: int, text: str | None, base_token: CommonToken):
        token: CommonToken = base_token.clone()
        token.type = type
        token.channel = channel
        token.stop = base_token.start - 1
        token.text = "<" + self.symbolicNames[type] + ">" if text is None else text
        self._addPendingToken(token)

    def _addPendingToken(self, token: CommonToken):
        self._lastPendingTokenType = token.type
        if token.channel == Token.DEFAULT_CHANNEL:
            self._lastPendingTokenTypeFromDefaultChannel = self._lastPendingTokenType
        self._pendingTokens.append(token)

    def _hideAndAddPendingToken(self, token: CommonToken):
        token.channel = Token.HIDDEN_CHANNEL
        self._addPendingToken(token)

    def _popPendingToken(self) -> CommonToken:
        return self._pendingTokens.pop(0)

    def _handle_NEWLINE_token(self):
        if self._numOpens > 0 or self._lastPendingTokenType in self._operators:
            self._hideAndAddPendingToken(self._currentToken)
        else:
            nl_token: CommonToken = self._currentToken
            is_looking_ahead: bool = self._followingToken.type == self.WS

            if is_looking_ahead:
                self._setNextInternalTokens()

            match self._followingToken.type:
                case self.NEWLINE | self.COMMENT:
                    self._hideAndAddPendingToken(nl_token)
                    if is_looking_ahead:
                        self._addPendingToken(self._currentToken)
                case _:
                    if is_looking_ahead:
                        indentation_length: int = (
                            0
                            if self._followingToken.type == Token.EOF
                            else self._getIndentationLength(self._currentToken.text)
                        )
                        if self._isValidIndent(indentation_length):
                            self._addPendingToken(nl_token)
                            self._addPendingToken(self._currentToken)
                            self._insertIndentOrDedentToken(indentation_length)
                        else:
                            self._hideAndAddPendingToken(nl_token)
                            self._addPendingToken(self._currentToken)
                    else:
                        self._addPendingToken(nl_token)
                        self._insertIndentOrDedentToken(0)

    def _isValidIndent(self, indent_length: int):
        return indent_length % self._indentLength == 0

    def _insertIndentOrDedentToken(self, indent_length: int):
        prev_indent_length: int = self._indentLengthStack[-1]
        if indent_length > prev_indent_length:
            self._createAndAddPendingToken(self.INDENT, Token.DEFAULT_CHANNEL, None, self._followingToken)
            self._indentLengthStack.append(indent_length)
        else:
            while indent_length < prev_indent_length:
                self._indentLengthStack.pop()
                prev_indent_length = self._indentLengthStack[-1]
                if indent_length <= prev_indent_length:
                    self._createAndAddPendingToken(self.DEDENT, Token.DEFAULT_CHANNEL, None, self._followingToken)
                else:
                    message = "inconsistent dedent"
                    self._reportLexerError(message, self._followingToken, IndentationError)
                    self._createAndAddPendingToken(
                        self.ERROR_TOKEN, Token.DEFAULT_CHANNEL, message, self._followingToken
                    )

    def _handle_STRING_token(self):
        replacedText: str = self._currentToken.text
        replacedText = re.sub(r"(\r?\n)+", r"\1", replacedText)
        replacedText = re.sub(r"(\r?\n)(\s)+", "", replacedText)
        if len(self._currentToken.text) == len(replacedText):
            self._addPendingToken(self._currentToken)
        else:
            originalToken: CommonToken = self._currentToken.clone()
            self._currentToken.text = replacedText
            self._addPendingToken(self._currentToken)
            self._hideAndAddPendingToken(originalToken)

    def _insertTrailingTokens(self):
        match self._lastPendingTokenTypeFromDefaultChannel:
            case self.NEWLINE | self.DEDENT:
                pass
            case _:
                self._createAndAddPendingToken(self.NEWLINE, Token.DEFAULT_CHANNEL, None, self._followingToken)
        self._insertIndentOrDedentToken(0)

    def _handle_EOF_token(self):
        if self._lastPendingTokenTypeFromDefaultChannel > 0:
            self._insertTrailingTokens()
        self._addPendingToken(self._currentToken)

    def _reportLexerError(self, message, token, errcls):
        lineno = token.line
        offset = token.column
        error = errcls(message) if errcls else None
        self.getErrorListenerDispatch().syntaxError(
            self,
            token,
            lineno,
            offset,
            message,
            error,
        )

    def reset(self):
        self._resetInternalStates()
        super().reset()
