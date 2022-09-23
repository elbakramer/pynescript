import glob

from pathlib import Path

from pytest import Parser, Metafunc


def pytest_addoption(parser: Parser):
    parser.addoption("--example-scripts-dir")


def pytest_generate_tests(metafunc: Metafunc):
    if "pinescript_filepath" in metafunc.fixturenames:
        example_scripts_dir = metafunc.config.getoption("--example-scripts-dir")
        if not example_scripts_dir:
            import pynescript

            module_dir = Path(pynescript.__file__).parent
            example_scripts_dir = module_dir / "data" / "builtin_scripts"
        pinescript_filepaths = glob.glob(str(example_scripts_dir / "*.pine"))
        metafunc.parametrize("pinescript_filepath", pinescript_filepaths)