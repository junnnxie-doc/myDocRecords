# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MyDoc'
copyright = '2024, junnnxie'
author = 'junnnxie'
release = '0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'zh-CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

html_static_path = ['_static']
# import sphinx_rtd_theme
# html_theme = "sphinx_rtd_theme"
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    'recommonmark',
    'sphinx_markdown_tables'
]
master_doc='index'
# source_suffix = {
#     '.rst': 'restructuredtext',
#     '.txt': 'markdown',
#     '.md': 'markdown',
# }