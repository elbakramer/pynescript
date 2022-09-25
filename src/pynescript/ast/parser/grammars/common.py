from pyparsing import Combine
from pyparsing import Empty
from pyparsing import Group
from pyparsing import Opt
from pyparsing import Suppress
from pyparsing import delimited_list

from pynescript.ast import types as ast
from pynescript.ast.parser.parser_elements import ConvertToNode
from pynescript.ast.parser.parser_elements import IndentedBlockWithTabs as IndentedBlock
from pynescript.ast.parser.parser_elements import ResultNameableForward as Forward
from pynescript.ast.parser.tokens import ARRAY
from pynescript.ast.parser.tokens import ASSIGN
from pynescript.ast.parser.tokens import BOOL
from pynescript.ast.parser.tokens import BOX
from pynescript.ast.parser.tokens import COLOR
from pynescript.ast.parser.tokens import COMMA
from pynescript.ast.parser.tokens import DOT
from pynescript.ast.parser.tokens import FLOAT
from pynescript.ast.parser.tokens import IDENTIFIER
from pynescript.ast.parser.tokens import INT
from pynescript.ast.parser.tokens import LABEL
from pynescript.ast.parser.tokens import LBRACKET
from pynescript.ast.parser.tokens import LCHEVRON
from pynescript.ast.parser.tokens import LINE
from pynescript.ast.parser.tokens import LINEFILL
from pynescript.ast.parser.tokens import LPAREN
from pynescript.ast.parser.tokens import MATRIX
from pynescript.ast.parser.tokens import RBRACKET
from pynescript.ast.parser.tokens import RCHEVRON
from pynescript.ast.parser.tokens import RPAREN
from pynescript.ast.parser.tokens import STRING
from pynescript.ast.parser.tokens import TABLE


expression = Forward()
local_statement = Forward()

type_specifier = Forward()
type_specifier.set_name("type_specifier")

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

atomic_type_name.set_name("atomic_type_name")

array_type_name = ConvertToNode(ast.Array)(ARRAY)
array_type_name.set_name("array_type_name")

matrix_type_name = ConvertToNode(ast.Matrix)(MATRIX)
matrix_type_name.set_name("matrix_type_name")

collection_type_name = array_type_name | matrix_type_name
collection_type_name.set_name("collection_type_name")

type_name = collection_type_name | atomic_type_name
type_name.set_name("type_name")

type_argument = Suppress(LCHEVRON) + type_specifier + Suppress(RCHEVRON)
type_argument.set_name("type_argument")

collection_type_specifier = ConvertToNode(ast.CollectionType)(
    collection_type_name("type_name") + type_argument("type_argument")
)
collection_type_specifier.set_name("collection_type_specifier")

array_type_suffix = Combine(LBRACKET + RBRACKET)
array_type_suffix.set_name("array_type_suffix")

array_type_specifier = ConvertToNode(ast.ArrayType)(
    Combine(type_specifier("element_type") + Suppress(array_type_suffix))
)
array_type_specifier.set_name("array_type_specifier")

atomic_type_specifier = atomic_type_name
atomic_type_specifier.set_name("atomic_type_specifier")

# this gives "ParseException raised: Forward recursion without base case, found '?' ..." error
type_specifier <<= (
    collection_type_specifier | array_type_specifier | atomic_type_specifier
)

# this solves the recursion problem above, but requires extra effort on parser action
type_specifier_trailing = Forward()
type_specifier_trailing <<= Opt(
    (array_type_suffix | type_argument) + type_specifier_trailing
)


def handle_type_specifier(results):
    last_token = results[-1]
    if len(results) == 1:
        return last_token
    else:
        results_except_last_token = results[:-1]
        if last_token == "[]":
            element_type_token = handle_type_specifier(results_except_last_token)
            return ast.ArrayType(element_type_token)
        else:
            type_name_token = handle_type_specifier(results_except_last_token)
            type_argument_token = last_token
            return ast.CollectionType(type_name_token, type_argument_token)


type_specifier <<= ConvertToNode(handle_type_specifier)(
    Group(type_name + type_specifier_trailing)
)


name = ConvertToNode(ast.Name)(IDENTIFIER)


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


attributed_name = ConvertToNode(handle_attributed_name)(
    Group(Empty() + delimited_list(name, DOT).leave_whitespace())
)


full_argument = IDENTIFIER("name") + Suppress(ASSIGN) + expression("value")
value_only_argument = expression("value")

argument = ConvertToNode(ast.Argument)(full_argument | value_only_argument)

argument_list = delimited_list(argument, COMMA)

function_call = ConvertToNode(ast.Call)(
    attributed_name("func")
    + Opt(type_argument("type_argument"))
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
local_body = local_block | local_statement

local_block.set_name("local_block")
local_body.set_name("local_body")
