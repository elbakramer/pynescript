from pyparsing import Empty
from pyparsing import LineEnd
from pyparsing import Literal


LPAREN = Literal("(")
RPAREN = Literal(")")

LCHEVRON = Literal("<")
RCHEVRON = Literal(">")

COMMA = Literal(",")
DOT = Literal(".")

DOUBLE_QUOTE = Literal('"')
SINGLE_QUOTE = Literal("'")

RIGHT_DOUBLE_ARROW = Literal("=>")

AT = Literal("@")
SHARP = Literal("#")

SPACE = Literal(" ")
TAB = Literal("\t")
ENTER = Literal("\n")

SLASH = Literal("/")
BACKSLASH = Literal("\\")

NEWLINE = LineEnd()
EMPTY = Empty()
