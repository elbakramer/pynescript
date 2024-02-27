from __future__ import annotations

import shutil

from pathlib import Path

from sphinx.application import Sphinx
from sphinx.ext.apidoc import main as sphinx_apidoc_main


project = "Pynescript"
author = "Yunseong Hwang"
copyright = "2024, Yunseong Hwang"  # noqa: A001
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"


def run_apidoc(_) -> None:
    docs_conf_path = Path(__file__)
    docs_dir = docs_conf_path.parent

    project_dir = docs_dir.parent

    output_path = project_dir / "docs/apidoc"
    module_path = project_dir / "src/pynescript"

    if output_path.exists():
        shutil.rmtree(output_path)

    args = [
        "--force",
        "--separate",
        "--ext-autodoc",
        "--output-dir",
        str(output_path),
        str(module_path),
    ]

    sphinx_apidoc_main(args)


def setup(app: Sphinx) -> None:
    app.connect("builder-inited", run_apidoc)
