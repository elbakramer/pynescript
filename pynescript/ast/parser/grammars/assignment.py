from pyparsing import (
    Forward,
    Opt,
)

from pynescript import ast
from pynescript.ast.parser.parser_elements import (
    ResultNameableForward as Forward,
    ConvertToNode,
)
from pynescript.ast.parser.tokens import (
    IDENTIFIER,
    VAR,
    VARIP,
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

type_specifier = Forward()
identifier_declarator = Forward()
tuple_declarator = Forward()
function_call = Forward()

declaration_mode = ConvertToNode(ast.Var)(VAR) | ConvertToNode(ast.VarIp)(VARIP)
declaration_mode.set_name("declaration_mode")

assignment_operator = ConvertToNode(ast.Assign)(ASSIGN)

identifier_declarator_declaration = ConvertToNode(ast.Assignment)(
    Opt(declaration_mode("declaration_mode"))
    + Opt(type_specifier("type_specifier"))
    + identifier_declarator("target")
    + assignment_operator("operator")
    + (structure | expression)("value")
)
identifier_declarator_declaration.set_name("identifier_declarator_declaration")

tuple_declarator_declaration = ConvertToNode(ast.Assignment)(
    tuple_declarator("target")
    + assignment_operator("operator")
    + (structure | function_call)("value")
)
tuple_declarator_declaration.set_name("tuple_declarator_declaration")

variable_declaration = identifier_declarator_declaration | tuple_declarator_declaration
variable_declaration.set_name("variable_declaration")

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
variable_reassignment.set_name("variable_reassignment")

assignment = variable_declaration | variable_reassignment
assignment.set_name("assignment")
