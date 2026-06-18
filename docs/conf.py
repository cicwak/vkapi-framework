from __future__ import annotations

import sys
from importlib.metadata import version as package_version
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

project = "vkapi"
copyright = "2026, Konstantin Ponomarev"
author = "Konstantin Ponomarev"

release = package_version("vkapi")
version = ".".join(release.split(".")[:2])

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

autodoc_member_order = "bysource"
autodoc_typehints = "description"
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = None

html_theme = "alabaster"
html_theme_options = {
    "github_user": "cicwak",
    "github_repo": "vkapi",
    "github_banner": True,
    "github_button": True,
    "github_type": "star",
    "fixed_sidebar": True,
}
html_static_path = ["_static"]
htmlhelp_basename = "vkapi"

latex_documents = [
    (master_doc, "vkapi.tex", "vkapi Documentation", author, "manual"),
]
man_pages = [(master_doc, "vkapi", "vkapi Documentation", [author], 1)]
texinfo_documents = [
    (
        master_doc,
        "vkapi",
        "vkapi Documentation",
        author,
        "vkapi",
        "Async-first VK API SDK and bot framework.",
        "Miscellaneous",
    ),
]
epub_title = project
epub_exclude_files = ["search.html"]
