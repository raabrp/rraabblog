#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

'''
This is our config file for [pelican](https://blog.getpelican.com/).

What happens here:

* We configure pelican to use the appropriate directories, paths, and settings
  for the repo. This means suppressing many of the bells and whistles (extra
  generated content) which are enabled by default.

* We define arbitrary (json-serializable) variables using python, which become:
  * globally accessable to Javascript (via the variable `pelican`)
  * accessable to Jinja templates (via `INJECTED` variable)

'''

import os
import sys
import json
import markdown

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import plugins

AUTHOR = 'Reilly Raab'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

###############################################################################
# PATHS

# content directory
# expected to have `articles` and `pages` subdirectories
PATH = 'content'
# additional subdirectories which are merely copied to output
STATIC_PATHS = ['images', 'static', 'js', 'css']
# File patterns which are ignored
IGNORE_FILES = ['.#*', '__pycache__']

# theme directory
# Expected to have `templates` and `static` subdirectories
THEME = 'theme'

# output directory
OUTPUT_PATH = 'public'

# path for plugins
PLUGIN_PATHS = ["plugins"]
# Plugin lists
PLUGINS = ["postprocess"]

###############################################################################
# Optional Config

# write original file sources to output
OUTPUT_SOURCES = True

# Markdown settings
MARKDOWN = {
    'extensions': [
        plugins.D3_MD_Extension(),     # inject D3 when needed
        plugins.Katex_MD_Extension(),  # process math with katex
        plugins.TWGL_MD_Extension(),   # inject TWGL when needed
        'toc',         # table of contents
        'footnotes',   # footnotes
        'tables',      # tables
        'fenced_code', # ``` codeblocks
        'codehilite',  # syntax higlighting
        'smarty'       # fancy quotes & stuff
    ],
    'extension_configs': {
        'toc': {
            'permalink': '#'
        },
        'smarty': {
            'smart_angled_quotes': True
        }
    },
    'output_format': 'html5'
}

# URL patterns
SLUGIFY_SOURCE = 'slug'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DRAFT_SAVE_AS = '{slug}.html'

# Suppress Categories and Tags
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
FEEDS_SAVE_AS = ''

# These templates render directly as independent output
DIRECT_TEMPLATES = ['index', 'links']

# Suppress unused utilities which Pelican provides
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
LINKS = None
SOCIAL = None
DEFAULT_PAGINATION = False

###############################################################################
# Personal variable injections

# Third party fonts
REMOTE_FONT_URL = "https://fonts.googleapis.com/css?family=Raleway:600i|Roboto"

# collect names of css files used for color themes
color_prefix = "color-"
color_suffix = ".css"
theme_names = sorted([
    x[len(color_prefix):-len(color_suffix)] for x in \
    os.listdir(os.path.join(THEME, 'static', 'css', 'colors')) \
    if x.startswith(color_prefix)
])

# JSON-serialiazable data available to Jinja templates
# (accessable to Jinja templates as variable `JINJA_INJECTED`)
JINJA_INJECTED = {
    'theme_names': theme_names
}

# JSON-serialiazable data available to javascript files
# (accessable to javascript as variable `pelican`)
JS_INJECTED = {}

# String which declares injected variables for javascript
INLINE_JS = 'var pelican = ' + json.dumps(JS_INJECTED) + ';'
