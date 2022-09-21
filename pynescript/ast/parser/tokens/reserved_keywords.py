from pyparsing import Keyword

from .type_keywords import (
    INT,
    FLOAT,
    BOOL,
    COLOR,
    STRING,
    LABEL,
    LINE,
    LINEFILL,
    ARRAY,
    MATRIX,
    BOX,
    TABLE,
)

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

KEYWORD = (
    AND
    | AS
    | ARRAY
    | BREAK
    | BY
    | CONST
    | CONTINUE
    | ELSE
    | EXPORT
    | FALSE
    | FOR
    | IN
    | IF
    | IMPORT
    | NA
    | NOT
    | OR
    | SERIES
    | SIMPLE
    | SWITCH
    | TO
    | TRUE
    | VAR
    | VARIP
    | WHILE
    | INT
    | FLOAT
    | BOOL
    | COLOR
    | STRING
    | LABEL
    | LINEFILL
    | LINE
    | MATRIX
    | BOX
    | TABLE
)

LITERAL_KEYWORD = TRUE | FALSE | NA

TYPE_KEYWORD = (
    INT | FLOAT | BOOL | COLOR | STRING | LABEL | LINEFILL | LINE | MATRIX | BOX | TABLE
)

SYNTAX_KEYWORD = (
    AND
    | AS
    | BREAK
    | BY
    | CONST
    | CONTINUE
    | ELSE
    | EXPORT
    | FOR
    | IN
    | IF
    | IMPORT
    | NOT
    | OR
    | SIMPLE
    | SWITCH
    | TO
    | VAR
    | VARIP
    | WHILE
)
