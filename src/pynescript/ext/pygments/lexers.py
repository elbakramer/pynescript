from typing import Iterable, Optional, Tuple

from pygments.lexer import Lexer
from pygments.token import Token, _TokenType

from pyparsing import ParserElement, ParseResults, TokenConverter
from pyparsing import Literal, Keyword, White, LineEnd
from pyparsing import MatchFirst, And, OneOrMore, Combine, FollowedBy, SkipTo, Suppress
from pyparsing import common

from pynescript.ast.parser.tokens import (
    INT,
    FLOAT,
    BOOL,
    STRING,
    COLOR,
    LABEL,
    LINE,
    BOX,
    LINEFILL,
    TABLE,
    ARRAY,
    MATRIX,
    CONST,
    SIMPLE,
    SERIES,
    IF,
    ELSE,
    SWITCH,
    FOR,
    TO,
    IN,
    BY,
    WHILE,
    BREAK,
    CONTINUE,
    IMPORT,
    AS,
    EXPORT,
    VAR,
    VARIP,
    TRUE,
    FALSE,
    NA,
    AND,
    NOT,
    OR,
    LITERAL_INT,
    LITERAL_FLOAT,
    LITERAL_BOOL,
    LITERAL_COLOR,
    LITERAL_STRING,
    IDENTIFIER,
    EQ,
    NEQ,
    LE,
    LT,
    GE,
    GT,
    ASSIGN,
    MOD,
    MUL,
    ADD,
    SUB,
    DIV,
    QUESTION,
    COLON,
    LBRACKET,
    RBRACKET,
    LPAREN,
    RPAREN,
    LCHEVRON,
    RCHEVRON,
    COMMA,
    DOT,
    RIGHT_DOUBLE_ARROW,
    SLASH,
)


TokenUnprocessed = Tuple[int, _TokenType, str]


class PyparsingToken(TokenConverter):
    def __init__(self, expr: ParserElement, token: Optional[_TokenType] = None) -> None:
        super().__init__(expr)
        self.token = token

    def postParse(self, instring: str, loc: int, tokenlist: ParseResults):
        if self.token is None:
            return []
        return [(loc, self.token, str(tokenlist[0]))]


class PinescriptLexer(Lexer):
    name = "Pinescript Lexer"
    aliases = "pinescript"
    filenames = ["*.pine"]

    white_expr = PyparsingToken(White(), Token.Text.Whitespace)
    version_comment_expr = And(
        [
            PyparsingToken(Literal("//"), Token.Comment),
            PyparsingToken(Literal("@"), Token.Punctuation),
            PyparsingToken(Keyword("version"), Token.Keyword),
            PyparsingToken(Literal("="), Token.Punctuation),
            PyparsingToken(common.integer("version"), Token.Literal.Number),
            PyparsingToken(FollowedBy(LineEnd())),
        ]
    )
    comment_expr = PyparsingToken(
        Combine(Literal("//") + SkipTo(LineEnd())("comment")), Token.Comment
    )
    token_expr = MatchFirst(
        [
            PyparsingToken(INT, Token.Keyword),
            PyparsingToken(FLOAT, Token.Keyword),
            PyparsingToken(BOOL, Token.Keyword),
            PyparsingToken(STRING, Token.Keyword),
            PyparsingToken(COLOR, Token.Keyword),
            PyparsingToken(LABEL, Token.Keyword),
            PyparsingToken(LINE, Token.Keyword),
            PyparsingToken(BOX, Token.Keyword),
            PyparsingToken(LINEFILL, Token.Keyword),
            PyparsingToken(TABLE, Token.Keyword),
            PyparsingToken(ARRAY, Token.Keyword),
            PyparsingToken(MATRIX, Token.Keyword),
            PyparsingToken(CONST, Token.Keyword),
            PyparsingToken(SIMPLE, Token.Keyword),
            PyparsingToken(SERIES, Token.Keyword),
            PyparsingToken(IF, Token.Keyword),
            PyparsingToken(ELSE, Token.Keyword),
            PyparsingToken(SWITCH, Token.Keyword),
            PyparsingToken(FOR, Token.Keyword),
            PyparsingToken(TO, Token.Keyword),
            PyparsingToken(IN, Token.Keyword),
            PyparsingToken(BY, Token.Keyword),
            PyparsingToken(WHILE, Token.Keyword),
            PyparsingToken(BREAK, Token.Keyword),
            PyparsingToken(CONTINUE, Token.Keyword),
            PyparsingToken(IMPORT, Token.Keyword),
            PyparsingToken(AS, Token.Keyword),
            PyparsingToken(EXPORT, Token.Keyword),
            PyparsingToken(VAR, Token.Keyword),
            PyparsingToken(VARIP, Token.Keyword),
            PyparsingToken(TRUE, Token.Keyword),
            PyparsingToken(FALSE, Token.Keyword),
            PyparsingToken(NA, Token.Keyword),
            PyparsingToken(AND, Token.Operator),
            PyparsingToken(NOT, Token.Operator),
            PyparsingToken(OR, Token.Operator),
            PyparsingToken(LITERAL_INT, Token.Literal.Number),
            PyparsingToken(LITERAL_FLOAT, Token.Literal.Number),
            PyparsingToken(LITERAL_BOOL, Token.Literal),
            PyparsingToken(LITERAL_COLOR, Token.Literal),
            PyparsingToken(LITERAL_STRING, Token.Literal.String),
            PyparsingToken(IDENTIFIER, Token.Name),
            PyparsingToken(EQ, Token.Operator),
            PyparsingToken(NEQ, Token.Operator),
            PyparsingToken(LE, Token.Operator),
            PyparsingToken(LT, Token.Operator),
            PyparsingToken(GE, Token.Operator),
            PyparsingToken(GT, Token.Operator),
            PyparsingToken(ASSIGN, Token.Operator),
            PyparsingToken(MOD, Token.Operator),
            PyparsingToken(MUL, Token.Operator),
            PyparsingToken(ADD, Token.Operator),
            PyparsingToken(SUB, Token.Operator),
            PyparsingToken(DIV, Token.Operator),
            PyparsingToken(QUESTION, Token.Operator),
            PyparsingToken(COLON, Token.Operator),
            PyparsingToken(LBRACKET, Token.Punctuation),
            PyparsingToken(RBRACKET, Token.Punctuation),
            PyparsingToken(LPAREN, Token.Punctuation),
            PyparsingToken(RPAREN, Token.Punctuation),
            PyparsingToken(LCHEVRON, Token.Punctuation),
            PyparsingToken(RCHEVRON, Token.Punctuation),
            PyparsingToken(COMMA, Token.Punctuation),
            PyparsingToken(DOT, Token.Punctuation),
            PyparsingToken(RIGHT_DOUBLE_ARROW, Token.Punctuation),
            PyparsingToken(SLASH, Token.Punctuation),
        ]
    )
    expr = white_expr | version_comment_expr | comment_expr | token_expr
    expr.leave_whitespace()

    def get_tokens_unprocessed(self, text: str) -> Iterable[TokenUnprocessed]:
        return OneOrMore(self.expr).parse_string(text, parse_all=True)

    @staticmethod
    def analyze_text(text: str) -> float:
        text_transformed = Suppress(PinescriptLexer.expr).transform_string(text)
        len_text = len(text)
        len_text_transformed = len(text_transformed)
        if len_text > 0:
            score = (len_text - len_text_transformed) / len_text
        else:
            score = 0.0
        return score
