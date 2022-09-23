"""Sphinx configuration."""
project = "Pynescript"
author = "Yunseong Hwang"
copyright = "2022, Yunseong Hwang"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
