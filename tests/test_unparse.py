from pynescript.ast.helpers import unparse
from pynescript.ast.parser.helpers import parse


def test_unparse(pinescript_filepath):
    parsed_ast = parse(pinescript_filepath, debug=True)
    unparsed_source = unparse(parsed_ast)
    reparsed_ast = parse(unparsed_source, debug=True)
    assert repr(parsed_ast) == repr(reparsed_ast)
