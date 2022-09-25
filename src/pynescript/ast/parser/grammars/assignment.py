from pyparsing import Combine
from pyparsing import Opt
from pyparsing import Suppress

from pynescript.ast import types as ast
from pynescript.ast.parser.parser_elements import ConvertToNode
from pynescript.ast.parser.parser_elements import ResultNameableForward as Forward
from pynescript.ast.parser.tokens import ADD
from pynescript.ast.parser.tokens import ASSIGN
from pynescript.ast.parser.tokens import COLON
from pynescript.ast.parser.tokens import DIV
from pynescript.ast.parser.tokens import IDENTIFIER
from pynescript.ast.parser.tokens import MOD
from pynescript.ast.parser.tokens import MUL
from pynescript.ast.parser.tokens import SUB
from pynescript.ast.parser.tokens import VAR
from pynescript.ast.parser.tokens import VARIP


expression = Forward()

type_specifier = Forward()

identifier_declarator = Forward()
tuple_declarator = Forward()

declaration_mode = ConvertToNode(ast.Var)(VAR) | ConvertToNode(ast.VarIp)(VARIP)
declaration_mode.set_name("declaration_mode")

assignment_operator = ASSIGN

identifier_declarator_declaration = ConvertToNode(ast.Assign)(
    Opt(declaration_mode("declaration_mode"))
    + Opt(type_specifier("type_specifier"))
    + identifier_declarator("target")
    + Suppress(assignment_operator)
    + expression("value")
)
identifier_declarator_declaration.set_name("identifier_declarator_declaration")

tuple_declarator_declaration = ConvertToNode(ast.Assign)(
    tuple_declarator("target") + Suppress(assignment_operator) + expression("value")
)
tuple_declarator_declaration.set_name("tuple_declarator_declaration")

variable_declaration = identifier_declarator_declaration | tuple_declarator_declaration
variable_declaration.set_name("variable_declaration")

aug_assignment_operator = (
    ConvertToNode(ast.Colon)(COLON)
    | ConvertToNode(ast.Mult)(MUL)
    | ConvertToNode(ast.Div)(DIV)
    | ConvertToNode(ast.Mod)(MOD)
    | ConvertToNode(ast.Add)(ADD)
    | ConvertToNode(ast.Sub)(SUB)
)

variable_reassignment = ConvertToNode(ast.AugAssign)(
    IDENTIFIER("target")
    + Combine(aug_assignment_operator("operator") + Suppress(assignment_operator))
    + expression("value")
)
variable_reassignment.set_name("variable_reassignment")

assignment = variable_declaration | variable_reassignment
assignment.set_name("assignment")
