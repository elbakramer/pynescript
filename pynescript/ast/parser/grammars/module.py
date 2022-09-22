from pyparsing import (
    Forward,
    Literal,
    Keyword,
    SkipTo,
    FollowedBy,
    Suppress,
    LineEnd,
    Group,
    ZeroOrMore,
)
from pyparsing import common

from pynescript import ast
from pynescript.ast.parser.parser_elements import (
    ResultNameableForward as Forward,
    ConvertToNode,
)

global_statement = Forward()

comment = Literal("//") + SkipTo(LineEnd())("comment")

comment_suppressed = Suppress(comment)

version_comment = (
    Literal("//")
    + Literal("@")
    + Keyword("version")
    + Literal("=")
    + common.integer("version")
    + FollowedBy(LineEnd())
)

script = ConvertToNode(ast.Script)(Group(ZeroOrMore(global_statement)))
