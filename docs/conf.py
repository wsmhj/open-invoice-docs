# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

project = "open-invoice-docs"
copyright = "2026, wsmhj"
author = "wsmhj"
release = "0.1.0"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = []

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")

myst_enable_extensions = [
    "deflist",
    "linkify",
]

myst_heading_anchors = 3
