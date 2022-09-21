from ast import literal_eval as python_literal_eval
from typing import Union, Callable

from pyparsing import (
    Literal,
    Word,
    Char,
    Combine,
    ZeroOrMore,
    OneOrMore,
    Opt,
    QuotedString,
    ParserElement,
)
from pyparsing import srange, quoted_string

from pynescript.ast.parser.parser_elements import (
    ConverterUsingFactory,
)

from pynescript.types import (
    PythonIntType,
    PythonFloatType,
    PythonBoolType,
    PythonStringType,
)

from pynescript.types import (
    IntType,
    FloatType,
    BoolType,
    ColorType,
    StringType,
)

from pynescript.ast.parser.utils import identity

from .fragments import D, L, H, E, FS, IS
from .reserved_keywords import TRUE, FALSE, SYNTAX_KEYWORD

PythonType = Union[PythonIntType, PythonFloatType, PythonBoolType, PythonStringType]
PynescriptType = Union[IntType, FloatType, BoolType, ColorType, StringType]

# identifier token

IDENTIFIER_COMBINE = Combine(L + ZeroOrMore(L | D))
IDENTIFIER_WORD = Word(L.initCharsOrig, L.initCharsOrig + D.initCharsOrig)

IDENTIFIER = Combine(~SYNTAX_KEYWORD + IDENTIFIER_WORD)
IDENTIFIER.set_name("IDENTIFIER")

# literal fragments

HEX = Combine(Literal("0") + Char(srange("[xX]")) + OneOrMore(H) + Opt(IS))
DEC = Combine(OneOrMore(D) + Opt(IS))

SCI_NO_POINT = Combine(OneOrMore(D) + E + Opt(FS))
SCI_OPT_POINT = Combine(ZeroOrMore(D) + Literal(".") + OneOrMore(D) + Opt(E) + Opt(FS))
SCI_POINT_OPT = Combine(OneOrMore(D) + Literal(".") + ZeroOrMore(D) + Opt(E) + Opt(FS))

# literal tokens

dbl_quoted_multiline_string = QuotedString(
    quote_char='"',
    esc_char=None,
    esc_quote="\\",
    multiline=True,
    unquote_results=False,
    end_quote_char=None,
    convert_whitespace_escapes=False,
)
sgl_quoted_multiline_string = QuotedString(
    quote_char="'",
    esc_char=None,
    esc_quote="\\",
    multiline=True,
    unquote_results=False,
    end_quote_char=None,
    convert_whitespace_escapes=False,
)

quoted_multiline_string = Combine(
    dbl_quoted_multiline_string | sgl_quoted_multiline_string
)

LITERAL_INT = HEX | DEC
LITERAL_FLOAT = SCI_NO_POINT | SCI_OPT_POINT | SCI_POINT_OPT
LITERAL_BOOL = TRUE | FALSE
LITERAL_COLOR = Combine(Literal("#") + (H * 6) + Opt(H * 2))
LITERAL_STRING = Combine(quoted_string | quoted_multiline_string)

# constant token


def token_to_python_int(string: str) -> PythonIntType:
    result = python_literal_eval(string)
    if not isinstance(result, PythonIntType):
        raise ValueError()
    return result


def token_to_python_float(string: str) -> PythonFloatType:
    result = python_literal_eval(string)
    if not isinstance(result, PythonFloatType):
        raise ValueError()
    return result


def token_to_python_string(string: str) -> PythonStringType:
    string = string.replace("\n", "")
    result = python_literal_eval(string)
    if not isinstance(result, PythonStringType):
        raise ValueError()
    return result


def token_to_python_bool(string: str) -> PythonBoolType:
    string = string.capitalize()
    result = python_literal_eval(string)
    if not isinstance(result, PythonBoolType):
        raise ValueError()
    return result


def make_constant_factory(
    token_to_python_value: Callable[PythonStringType, PythonType],
    python_value_to_value: Callable[PythonType, PynescriptType],
):
    def factory(token):
        python_value = token_to_python_value(token)
        value = python_value_to_value(python_value)
        return value

    return factory


class ParseInt(ConverterUsingFactory[PynescriptType]):
    def __init__(self, expr: ParserElement):
        factory = make_constant_factory(token_to_python_int, IntType)
        super().__init__(expr, factory)


class ParseFloat(ConverterUsingFactory[PynescriptType]):
    def __init__(self, expr: ParserElement):
        factory = make_constant_factory(token_to_python_float, FloatType)
        super().__init__(expr, factory)


class ParseBool(ConverterUsingFactory[PynescriptType]):
    def __init__(self, expr: ParserElement):
        factory = make_constant_factory(token_to_python_bool, BoolType)
        super().__init__(expr, factory)


class ParseColor(ConverterUsingFactory[PynescriptType]):
    def __init__(self, expr: ParserElement):
        factory = make_constant_factory(identity, ColorType)
        super().__init__(expr, factory)


class ParseString(ConverterUsingFactory[PynescriptType]):
    def __init__(self, expr: ParserElement):
        factory = make_constant_factory(token_to_python_string, StringType)
        super().__init__(expr, factory)


CONSTANT = (
    ParseFloat(LITERAL_FLOAT)
    | ParseInt(LITERAL_INT)
    | ParseBool(LITERAL_BOOL)
    | ParseString(LITERAL_STRING)
    | ParseColor(LITERAL_COLOR)
)
CONSTANT.set_name("CONSTANT")
