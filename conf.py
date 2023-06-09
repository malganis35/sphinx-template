# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import date

# -- Project information -----------------------------------------------------

project = 'Sphinx Template Website'
copyright = f'{date.today().year}, Cao Tri DO'
author = 'Cao Tri DO'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.viewcode',
    'sphinx_git',
    'sphinx_inline_tabs',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton',
    'sphinx_favicon',
    'nbsphinx',
    'sphinx_last_updated_by_git',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 
                    '*/README.rst', 'README.rst', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'furo'
# html_theme = 'sphinx_book_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = []
html_static_path = ['_static']

# By default, generated HTML <title> has the value project release documentation. E.g. Tech writer at work 1.0 documentation.
# If you don’t have conf.py’s release set, it is e.g., Tech writer at work  documentation (please note two spaces among “work” and “documentation”).
# If you don’t like word “documentation” or two-space issue, you have to set custom title in html_title conf.py option. For example, let’s set it to the same value as a project option.
html_title = project

# Code examples are highlighted by default syntax highlight language, if not configured otherwise for a particular example. Sphinx default syntax highlighting mode is 'python3'.
# Maybe as Sphinx is mainly used in Python projects, it is reasonable value, but I personally almost always change it to ''none'' that turns off syntax highlighting
highlight_language = 'none'


# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ".aspx"


favicons = [
    {"href": "logo_Destination-Familles-favicon.png"},  # => use `_static/icon.svg`
]


html_use_index = True