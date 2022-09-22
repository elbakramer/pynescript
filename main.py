import glob
import random

from pathlib import Path

import pynescript

from pynescript.ast.parser.helpers import parse


def test_random_file():
    module_dir = Path(pynescript.__file__).parent
    builtint_scripts_dir = module_dir / "data" / "builtin_scripts"

    builtin_script_filepaths = glob.glob(str(builtint_scripts_dir / "*.pine"))
    builtin_script_filepaths_count = len(builtin_script_filepaths)

    script_index = random.randrange(builtin_script_filepaths_count)
    script_filepath = builtin_script_filepaths[script_index]

    res = parse(script_filepath, parse_all=True)

    print(res)
    print(script_filepath)


if __name__ == "__main__":
    test_random_file()
