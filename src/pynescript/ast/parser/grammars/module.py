from pyparsing import FollowedBy
from pyparsing import Group
from pyparsing import Keyword
from pyparsing import LineEnd
from pyparsing import Literal
from pyparsing import SkipTo
from pyparsing import Suppress
from pyparsing import ZeroOrMore
from pyparsing import common

from pynescript.ast import types as ast
from pynescript.ast.parser.parser_elements import ConvertToNode
from pynescript.ast.parser.parser_elements import ResultNameableForward as Forward


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
