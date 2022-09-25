from pyparsing import Group
from pyparsing import Opt
from pyparsing import Suppress
from pyparsing import delimited_list

from pynescript.ast import types as ast
from pynescript.ast.parser.parser_elements import ConvertToNode
from pynescript.ast.parser.parser_elements import ResultNameableForward as Forward
from pynescript.ast.parser.tokens import AS
from pynescript.ast.parser.tokens import ASSIGN
from pynescript.ast.parser.tokens import BREAK
from pynescript.ast.parser.tokens import COMMA
from pynescript.ast.parser.tokens import CONTINUE
from pynescript.ast.parser.tokens import IDENTIFIER
from pynescript.ast.parser.tokens import IMPORT
from pynescript.ast.parser.tokens import LPAREN
from pynescript.ast.parser.tokens import RIGHT_DOUBLE_ARROW
from pynescript.ast.parser.tokens import RPAREN
from pynescript.ast.parser.tokens import SLASH


assignment = Forward()
expression = Forward()

local_body = Forward()

assignment_statement = assignment

expression_statement = ConvertToNode(ast.Expr)(expression("value"))

common_statement = assignment_statement | expression_statement
common_statement.set_name("common_statement")

import_statement = (
    Suppress(IMPORT)
    + IDENTIFIER
    + Suppress(SLASH)
    + IDENTIFIER
    + Suppress(SLASH)
    + IDENTIFIER
    + Suppress(AS)
    + IDENTIFIER
)
import_statement.set_name("import_statement")

default_value = expression

full_parameter_declaration = (
    IDENTIFIER("name") + Suppress(ASSIGN) + default_value("default_value")
)

name_only_parameter_declaration = IDENTIFIER("name")

parameter_declaration = ConvertToNode(ast.Parameter)(
    full_parameter_declaration | name_only_parameter_declaration
)

parameter_declaration.set_name("parameter_declaration")

parameter_list = delimited_list(parameter_declaration, COMMA)

function_declaration = ConvertToNode(ast.FunctionDef)(
    IDENTIFIER("name")
    + Suppress(LPAREN)
    + Opt(parameter_list("parameters"))
    + Suppress(RPAREN)
    + Suppress(RIGHT_DOUBLE_ARROW)
    + Group(local_body)("body")
)
function_declaration.set_name("function_declaration")

global_only_statement = import_statement | function_declaration

break_statement = ConvertToNode(ast.Break)(BREAK)
continue_statement = ConvertToNode(ast.Continue)(CONTINUE)

jump_statement = break_statement | continue_statement

local_only_statement = jump_statement

global_atomic_statement = global_only_statement | common_statement
local_atomic_statement = local_only_statement | common_statement

global_atomic_statement.set_name("global_atomic_statement")
local_atomic_statement.set_name("local_atomic_statement")

global_statement = delimited_list(global_atomic_statement, COMMA)
local_statement = delimited_list(local_atomic_statement, COMMA)

global_statement.set_name("global_statement")
local_statement.set_name("local_statement")
