from pyparsing import (
    Forward,
    Literal,
    Keyword,
    FollowedBy,
    LineEnd,
    Group,
    ZeroOrMore,
)
from pyparsing import common

from pynescript import ast
from pynescript.ast.parser.parser_elements import (
    ConvertToNode,
)

global_statement = Forward()

comment = Literal("//") + ... + FollowedBy(LineEnd())

version_comment = (
    Literal("//")
    + Literal("@")
    + Keyword("version")
    + Literal("=")
    + common.integer("version")
    + FollowedBy(LineEnd())
)

script = ConvertToNode(ast.Script)(Group(ZeroOrMore(global_statement)))

script.ignore(comment)
