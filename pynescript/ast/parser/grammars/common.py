from pyparsing import (
    Forward,
    Suppress,
    Group,
    Opt,
    Empty,
    IndentedBlock,
)
from pyparsing import delimited_list

from pynescript import ast
from pynescript.ast.parser.parser_elements import (
    ConvertToNode,
)
from pynescript.ast.parser.tokens import (
    IDENTIFIER,
    DOT,
    COMMA,
    ASSIGN,
    LBRACKET,
    RBRACKET,
    INT,
    FLOAT,
    BOOL,
    STRING,
    COLOR,
    LABEL,
    LINEFILL,
    LINE,
    BOX,
    TABLE,
    ARRAY,
    MATRIX,
    LCHEVRON,
    RCHEVRON,
    LPAREN,
    RPAREN,
)

expression = Forward()
local_statement = Forward()

atomic_type_name = (
    ConvertToNode(ast.Int)(INT)
    | ConvertToNode(ast.Float)(FLOAT)
    | ConvertToNode(ast.Bool)(BOOL)
    | ConvertToNode(ast.String)(STRING)
    | ConvertToNode(ast.Color)(COLOR)
    | ConvertToNode(ast.Label)(LABEL)
    | ConvertToNode(ast.Linefill)(LINEFILL)
    | ConvertToNode(ast.Line)(LINE)
    | ConvertToNode(ast.Box)(BOX)
    | ConvertToNode(ast.Table)(TABLE)
)

array_type_name = ConvertToNode(ast.Array)(ARRAY)
matrix_type_name = ConvertToNode(ast.Matrix)(MATRIX)

collection_type_name = array_type_name | matrix_type_name

type_argument = Suppress(LCHEVRON) + atomic_type_name + Suppress(RCHEVRON)

name = ConvertToNode(ast.Name)(IDENTIFIER)
attributed_name = Empty() + delimited_list(name, DOT).leave_whitespace()


@attributed_name.set_parse_action
def handle_attributed_name(results):
    node = results[0]
    for attr in results[1:]:
        lineno = node.lineno
        col_offset = node.col_offset
        node = ast.Attribute(node, attr.id)
        end_lineno = attr.end_lineno
        end_col_offset = attr.end_col_offset
        node.set_attributes(
            lineno=lineno,
            col_offset=col_offset,
            end_lineno=end_lineno,
            end_col_offset=end_col_offset,
        )
    return node


full_argument = IDENTIFIER("name") + Suppress(ASSIGN) + expression("value")
value_only_argument = expression("value")

argument = ConvertToNode(ast.Argument)(full_argument | value_only_argument)

argument_list = delimited_list(argument, COMMA)

function_call = ConvertToNode(ast.Call)(
    attributed_name("name")
    + Opt(type_argument)
    + Suppress(LPAREN)
    + Opt(argument_list("arguments"))
    + Suppress(RPAREN)
)

identifier_declarator = IDENTIFIER
identifier_list = delimited_list(IDENTIFIER, COMMA)

tuple_declarator = ConvertToNode(ast.Tuple)(
    Suppress(LBRACKET) + identifier_list("values") + Suppress(RBRACKET)
)
tuple_declarator.set_name("tuple_declarator")

declarator = tuple_declarator | identifier_declarator

local_block = IndentedBlock(local_statement)
local_body = local_block | Group(local_statement)

local_block.set_name("local_block")
local_body.set_name("local_body")
