from pyparsing import Keyword
from pyparsing import MatchFirst


AND = Keyword("and")
AS = Keyword("as")
BREAK = Keyword("break")
BY = Keyword("by")
CONST = Keyword("const")
CONTINUE = Keyword("continue")
ELSE = Keyword("else")
EXPORT = Keyword("export")
FALSE = Keyword("false")
FOR = Keyword("for")
IN = Keyword("in")
IF = Keyword("if")
IMPORT = Keyword("import")
NA = Keyword("na")
NOT = Keyword("not")
OR = Keyword("or")
SERIES = Keyword("series")
SIMPLE = Keyword("simple")
SWITCH = Keyword("switch")
TO = Keyword("to")
TRUE = Keyword("true")
VAR = Keyword("var")
VARIP = Keyword("varip")
WHILE = Keyword("while")

SYNTAX_KEYWORD = MatchFirst(
    [
        AND,
        AS,
        BREAK,
        BY,
        CONST,
        CONTINUE,
        ELSE,
        EXPORT,
        FOR,
        IN,
        IF,
        IMPORT,
        NOT,
        OR,
        SIMPLE,
        SWITCH,
        TO,
        VAR,
        VARIP,
        WHILE,
    ]
)
