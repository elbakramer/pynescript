from pyparsing import Forward
from pyparsing import Opt

from pynescript.ast import types as ast
from pynescript.ast.parser.parser_elements import ConvertToNode
from pynescript.ast.parser.parser_elements import ResultNameableForward as Forward
from pynescript.ast.parser.tokens import ADD_ASSIGN
from pynescript.ast.parser.tokens import ASSIGN
from pynescript.ast.parser.tokens import COLON_ASSIGN
from pynescript.ast.parser.tokens import DIV_ASSIGN
from pynescript.ast.parser.tokens import IDENTIFIER
from pynescript.ast.parser.tokens import MOD_ASSIGN
from pynescript.ast.parser.tokens import MUL_ASSIGN
from pynescript.ast.parser.tokens import SUB_ASSIGN
from pynescript.ast.parser.tokens import VAR
from pynescript.ast.parser.tokens import VARIP


expression = Forward()

type_specifier = Forward()

identifier_declarator = Forward()
tuple_declarator = Forward()

declaration_mode = ConvertToNode(ast.Var)(VAR) | ConvertToNode(ast.VarIp)(VARIP)
declaration_mode.set_name("declaration_mode")

assignment_operator = ConvertToNode(ast.Assign)(ASSIGN)

identifier_declarator_declaration = ConvertToNode(ast.Assignment)(
    Opt(declaration_mode("declaration_mode"))
    + Opt(type_specifier("type_specifier"))
    + identifier_declarator("target")
    + assignment_operator("operator")
    + expression("value")
)
identifier_declarator_declaration.set_name("identifier_declarator_declaration")

tuple_declarator_declaration = ConvertToNode(ast.Assignment)(
    tuple_declarator("target") + assignment_operator("operator") + expression("value")
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
    IDENTIFIER("target") + reassignment_operator("operator") + expression("value")
)
variable_reassignment.set_name("variable_reassignment")

assignment = variable_declaration | variable_reassignment
assignment.set_name("assignment")
