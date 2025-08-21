# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pydata-visualizer'
copyright = '2025, Aditya Deshmukh'
author = 'Aditya Deshmukh'
release = '0.2.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',  # to understand .md files
    'sphinx.ext.autodoc',  # for automatic API documentation generation
    'sphinx.ext.viewcode',  # to show source code
    'sphinx.ext.napoleon',  # for Google/NumPy style docstrings
    'sphinx.ext.intersphinx',  # for linking between docs
]

# MyST Markdown settings
myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'tasklist',
    'smartquotes',
]
myst_heading_anchors = 3

templates_path = ['_templates']
exclude_patterns = []
source_suffix = ['.rst', '.md']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
