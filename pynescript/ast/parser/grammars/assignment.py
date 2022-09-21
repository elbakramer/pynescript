from pyparsing import (
    Forward,
    Suppress,
    Combine,
    Opt,
)

from pynescript import ast
from pynescript.ast.parser.parser_elements import (
    ConvertToNode,
)
from pynescript.ast.parser.tokens import (
    IDENTIFIER,
    VAR,
    VARIP,
    LBRACKET,
    RBRACKET,
    ASSIGN,
    COLON_ASSIGN,
    MUL_ASSIGN,
    DIV_ASSIGN,
    MOD_ASSIGN,
    ADD_ASSIGN,
    SUB_ASSIGN,
)

structure = Forward()
expression = Forward()

atomic_type_name = Forward()
collection_type_name = Forward()
type_argument = Forward()
identifier_declarator = Forward()
tuple_declarator = Forward()
function_call = Forward()


declaration_mode = ConvertToNode(ast.Var)(VAR) | ConvertToNode(ast.VarIp)(VARIP)


def handle_array_type_specifier(argument):
    node = ast.TypeReference(ast.Subscript(argument))
    return node


array_type_specifier = ConvertToNode(handle_array_type_specifier)(
    Combine(atomic_type_name("value") + Suppress(Combine(LBRACKET + RBRACKET)))
)

collection_type_specifier = ConvertToNode(ast.TypeReference)(
    collection_type_name("name") + type_argument("argument")
)

atomic_type_specifier = ConvertToNode(ast.TypeReference)(atomic_type_name("name"))

type_specifier = (
    collection_type_specifier | array_type_specifier | atomic_type_specifier
)

assignment_operator = ConvertToNode(ast.Assign)(ASSIGN)

identifier_declarator_declaration = ConvertToNode(ast.Assignment)(
    Opt(declaration_mode("declaration_mode"))
    + Opt(type_specifier("type_specifier"))
    + identifier_declarator("target")
    + assignment_operator("operator")
    + (structure | expression)("value")
)

tuple_declarator_declaration = ConvertToNode(ast.Assignment)(
    tuple_declarator("target")
    + assignment_operator("operator")
    + (structure | function_call)("value")
)

variable_declaration = identifier_declarator_declaration | tuple_declarator_declaration

reassignment_operator = (
    ConvertToNode(ast.ColonAssign)(COLON_ASSIGN)
    | ConvertToNode(ast.MultAssign)(MUL_ASSIGN)
    | ConvertToNode(ast.DivAssign)(DIV_ASSIGN)
    | ConvertToNode(ast.ModAssign)(MOD_ASSIGN)
    | ConvertToNode(ast.AddAssign)(ADD_ASSIGN)
    | ConvertToNode(ast.SubAssign)(SUB_ASSIGN)
)

variable_reassignment = ConvertToNode(ast.Assignment)(
    IDENTIFIER("target")
    + reassignment_operator("operator")
    + (structure | expression)("value")
)

assignment = variable_declaration | variable_reassignment
