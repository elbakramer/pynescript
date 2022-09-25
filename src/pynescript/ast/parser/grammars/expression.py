from pyparsing import OpAssoc
from pyparsing import Suppress
from pyparsing import delimited_list
from pyparsing import infix_notation

from pynescript.ast import types as ast
from pynescript.ast.parser.parser_elements import ConvertToNode
from pynescript.ast.parser.parser_elements import ResultNameableForward as Forward
from pynescript.ast.parser.tokens import ADD
from pynescript.ast.parser.tokens import AND
from pynescript.ast.parser.tokens import COLON
from pynescript.ast.parser.tokens import COMMA
from pynescript.ast.parser.tokens import CONSTANT
from pynescript.ast.parser.tokens import DIV
from pynescript.ast.parser.tokens import EQ
from pynescript.ast.parser.tokens import GE
from pynescript.ast.parser.tokens import GT
from pynescript.ast.parser.tokens import LBRACKET
from pynescript.ast.parser.tokens import LE
from pynescript.ast.parser.tokens import LPAREN
from pynescript.ast.parser.tokens import LT
from pynescript.ast.parser.tokens import MOD
from pynescript.ast.parser.tokens import MUL
from pynescript.ast.parser.tokens import NEQ
from pynescript.ast.parser.tokens import NOT
from pynescript.ast.parser.tokens import OR
from pynescript.ast.parser.tokens import QUESTION
from pynescript.ast.parser.tokens import RBRACKET
from pynescript.ast.parser.tokens import RPAREN
from pynescript.ast.parser.tokens import SUB


attributed_name = Forward()

function_call = Forward()
structure = Forward()

expression = Forward()
expression.set_name("expression")

unary_expression = Forward()
conditional_expression = Forward()

constant_expression = ConvertToNode(ast.Constant)(CONSTANT)

load_name_expression = attributed_name

history_referencing_expression = ConvertToNode(ast.Subscript)(
    attributed_name("value")
    + Suppress(LBRACKET)
    + expression("index")
    + Suppress(RBRACKET)
)

grouped_expression = Suppress(LPAREN) + expression + Suppress(RPAREN)

expression_list = delimited_list(expression, COMMA)

tuple_expression = ConvertToNode(ast.Tuple)(
    Suppress(LBRACKET) + expression_list("values") + Suppress(RBRACKET)
)

function_call_expression = function_call
structure_expression = structure

primary_expression = (
    constant_expression
    | tuple_expression
    | grouped_expression
    | function_call_expression
    | history_referencing_expression
    | load_name_expression
)

unary_operator = (
    ConvertToNode(ast.UAdd)(ADD)
    | ConvertToNode(ast.USub)(SUB)
    | ConvertToNode(ast.Not)(NOT)
)

unary_expression_pattern = ConvertToNode(ast.Unary)(
    unary_operator("operator") + unary_expression("operand")
)

unary_expression <<= unary_expression_pattern | primary_expression

multiplicative_operator = (
    ConvertToNode(ast.Mult)(MUL)
    | ConvertToNode(ast.Div)(DIV)
    | ConvertToNode(ast.Mod)(MOD)
)

additive_operator = ConvertToNode(ast.Add)(ADD) | ConvertToNode(ast.Sub)(SUB)

relational_operator = (
    ConvertToNode(ast.LessThanEqual)(LE)
    | ConvertToNode(ast.GreaterThanEqual)(GE)
    | ConvertToNode(ast.LessThan)(LT)
    | ConvertToNode(ast.GreaterThan)(GT)
)

equality_operator = ConvertToNode(ast.Equal)(EQ) | ConvertToNode(ast.NotEqual)(NEQ)

logical_and_operator = ConvertToNode(ast.And)(AND)

logical_or_operator = ConvertToNode(ast.Or)(OR)


def handle_relational_expression(left, operator, right):
    operators = [operator]
    comparators = [right]
    node = ast.Compare(left, operators, comparators)
    if isinstance(left, ast.Compare):
        left = left.left
        operators = left.operators + node.operators
        comparators = left.comparators + node.comparators
        node = ast.Compare(left, operators, comparators)
    return node


def iterate_logical_expression_values(values, operator):
    for value in values:
        if isinstance(value, ast.Boolean) and type(value.operator) is type(operator):
            yield from iterate_logical_expression_values(value.values, operator)
        else:
            yield value


def handle_logical_expression(left, operator, right):
    values = [left, right]
    values = iterate_logical_expression_values(values, operator)
    values = list(values)
    node = ast.Boolean(operator, values)
    return node


def infix_notation_action(action):
    def action_wrapper(tokenlist):
        tokenlist = tokenlist[0]
        node = action(tokenlist[0], tokenlist[1], tokenlist[2])
        tokenlist = tokenlist[3:]
        while tokenlist:
            node = action(node, tokenlist[0], tokenlist[1])
            tokenlist = tokenlist[2:]
        return node

    return action_wrapper


infix_notation_op_list = [
    (
        multiplicative_operator,
        2,
        OpAssoc.LEFT,
        infix_notation_action(ast.Binary),
    ),
    (
        additive_operator,
        2,
        OpAssoc.LEFT,
        infix_notation_action(ast.Binary),
    ),
    (
        relational_operator,
        2,
        OpAssoc.LEFT,
        infix_notation_action(handle_relational_expression),
    ),
    (equality_operator, 2, OpAssoc.LEFT, infix_notation_action(ast.Binary)),
    (
        logical_and_operator,
        2,
        OpAssoc.LEFT,
        infix_notation_action(handle_logical_expression),
    ),
    (
        logical_or_operator,
        2,
        OpAssoc.LEFT,
        infix_notation_action(handle_logical_expression),
    ),
]

infix_notation_expression = infix_notation(
    unary_expression, infix_notation_op_list, Suppress(LPAREN), Suppress(RPAREN)
)
infix_notation_expression.set_name("infix_notation_expression")

multiplicative_expression = Forward()
additive_expression = Forward()
relational_expression = Forward()
equality_expression = Forward()
logical_and_expression = Forward()
logical_or_expression = Forward()

multiplicative_expression.set_name("multiplicative_expression")
additive_expression.set_name("additive_expression")
relational_expression.set_name("relational_expression")
equality_expression.set_name("equality_expression")
logical_and_expression.set_name("logical_and_expression")
logical_or_expression.set_name("logical_or_expression")

multiplicative_expression_pattern = ConvertToNode(ast.Binary)(
    multiplicative_expression("left")
    + multiplicative_operator("operator")
    + unary_expression("right")
)

multiplicative_expression <<= multiplicative_expression_pattern | unary_expression

additive_expression_pattern = ConvertToNode(ast.Binary)(
    additive_expression("left")
    + additive_operator("operator")
    + multiplicative_expression("right")
)

additive_expression <<= additive_expression | multiplicative_expression

relational_expression_pattern = ConvertToNode(handle_relational_expression)(
    relational_expression("left")
    + relational_operator("operator")
    + additive_expression("right")
)

relational_expression <<= relational_expression_pattern | additive_expression

equality_expression_pattern = ConvertToNode(ast.Binary)(
    equality_expression("left")
    + equality_operator("operator")
    + relational_expression("right")
)

equality_expression <<= equality_expression_pattern | relational_expression

logical_and_expression_pattern = ConvertToNode(handle_logical_expression)(
    logical_and_expression("left")
    + logical_and_operator("operator")
    + equality_expression("right")
)

logical_and_expression <<= logical_and_expression | equality_expression

logical_or_expression_pattern = ConvertToNode(handle_logical_expression)(
    logical_or_expression("left")
    + logical_or_operator("operator")
    + logical_and_expression("right")
)

logical_or_expression <<= logical_or_expression_pattern | logical_and_expression

conditional_expression_pattern = ConvertToNode(ast.Ternary)(
    infix_notation_expression("condition")
    + Suppress(QUESTION)
    + expression("true_value")
    + Suppress(COLON)
    + conditional_expression("false_value")
)

conditional_expression <<= conditional_expression_pattern | infix_notation_expression

expression <<= structure_expression | conditional_expression
