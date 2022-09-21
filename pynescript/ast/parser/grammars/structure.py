from pyparsing import (
    Forward,
    Suppress,
    Group,
    Opt,
    IndentedBlock,
)

from pynescript import ast
from pynescript.ast.parser.tokens import (
    IF,
    ELSE,
    RIGHT_DOUBLE_ARROW,
    SWITCH,
    FOR,
    ASSIGN,
    TO,
    IN,
    BY,
    WHILE,
)
from pynescript.ast.parser.parser_elements import (
    ConvertToNode,
)

expression = Forward()

local_block = Forward()
local_body = Forward()
identifier_declarator = Forward()
declarator = Forward()

if_structure = Forward()

if_structure_impl = ConvertToNode(ast.If)(
    Suppress(IF)
    + expression("condition")
    + local_block("body")
    + Opt(Suppress(ELSE) + (Group(if_structure) | local_block)("orelse"))
)
if_structure_impl.set_name("if_structure")

if_structure <<= if_structure_impl

expression_switch_case = ConvertToNode(ast.SwitchCase)(
    expression("expression") + Suppress(RIGHT_DOUBLE_ARROW) + local_body("body")
)
default_switch_case = ConvertToNode(ast.SwitchCase)(
    Suppress(RIGHT_DOUBLE_ARROW) + local_body("body")
)
switch_case = default_switch_case | expression_switch_case

switch_structure_cases = IndentedBlock(switch_case)

switch_structure_with_expression = ConvertToNode(ast.Switch)(
    Suppress(SWITCH) + expression("expression") + switch_structure_cases("cases")
)

switch_structure_without_expression = ConvertToNode(ast.Switch)(
    Suppress(SWITCH) + switch_structure_cases("cases")
)

switch_structure = (
    switch_structure_with_expression | switch_structure_without_expression
)

conditional_structure = if_structure | switch_structure

for_statement_from_to_by = (
    identifier_declarator("target")
    + Suppress(ASSIGN)
    + expression("initial_value")
    + Suppress(TO)
    + expression("final_value")
    + Opt(Suppress(BY) + expression("increment_value"))
)

for_statement_in = declarator("target") + Suppress(IN) + expression("initial_value")

for_structure = ConvertToNode(ast.For)(
    Suppress(FOR) + (for_statement_from_to_by | for_statement_in) + local_block("body")
)

for_structure.set_name("for_structure")

while_structure = ConvertToNode(ast.While)(
    Suppress(WHILE) + expression("condition") + local_block("body")
)

loop_structure = for_structure | while_structure

structure = conditional_structure | loop_structure
