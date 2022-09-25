from pathlib import Path

from pytest import Metafunc
from pytest import Parser


def pytest_addoption(parser: Parser):
    parser.addoption("--example-scripts-dir")


def pytest_generate_tests(metafunc: Metafunc):
    if "pinescript_filepath" in metafunc.fixturenames:
        example_scripts_dir = metafunc.config.getoption("--example-scripts-dir")
        if not example_scripts_dir:
            tests_dir = Path(__file__).parent
            example_scripts_dir = tests_dir / "data" / "builtin_scripts"
        pinescript_filepaths = example_scripts_dir.glob("*.pine")
        metafunc.parametrize("pinescript_filepath", pinescript_filepaths)
