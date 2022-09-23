from pynescript.ast.parser.helpers import parse


def test_parse(pinescript_filepath):
    parse(pinescript_filepath, debug=True)
