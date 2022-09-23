import glob
import random

from pathlib import Path

import pynescript

from pynescript.ast import dump
from pynescript.ast import parse


def test_random_file():
    module_dir = Path(pynescript.__file__).parent
    builtint_scripts_dir = module_dir / "data" / "builtin_scripts"

    builtin_script_filepaths = glob.glob(str(builtint_scripts_dir / "*.pine"))
    builtin_script_filepaths_count = len(builtin_script_filepaths)

    script_index = random.randrange(builtin_script_filepaths_count)
    script_filepath = builtin_script_filepaths[script_index]

    tree = parse(script_filepath, debug=True)

    print(script_filepath)
    print(dump(tree, indent=2))


if __name__ == "__main__":
    test_random_file()
