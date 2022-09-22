import os
import glob
import contextlib

import pytest

import pyparsing
import pynescript


@contextlib.contextmanager
def not_raises(exception):
    try:
        yield
    except exception:
        raise pytest.fail("DID RAISE {0}".format(exception)) from exception


@pytest.fixture(name="builtin_scripts_dir")
def fixture_builtin_scripts_dir():
    module_dir = os.path.dirname(pynescript.__file__)
    scripts_dir = os.path.join(module_dir, "data", "builtin_scripts")
    return scripts_dir


def test_parse(builtin_scripts_dir):
    from pyparsing.exceptions import ParseException
    from pynescript.ast.parser.helpers import parse

    pyparsing.enable_all_warnings()

    builtin_script_filepaths = glob.glob(os.path.join(builtin_scripts_dir, "*.pine"))
    builtin_script_filepaths_count = len(builtin_script_filepaths)

    exception_count = 0

    for i, filepath in enumerate(builtin_script_filepaths):
        filename = os.path.basename(filepath)

        with open(filepath, encoding="utf-8") as f:
            code = f.read()

        try:
            parse(code, debug=True)
        except ParseException:
            exception_count += 1
            print(f"FAIL ({i + 1}/{builtin_script_filepaths_count}): {filename}")
            raise
        else:
            print(f"PASS ({i + 1}/{builtin_script_filepaths_count}): {filename}")

    if exception_count > 0:
        raise pytest.fail(
            f"Total fails: {exception_count}/{builtin_script_filepaths_count}"
        )
