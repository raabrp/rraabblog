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

sys.path.append(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'plugins'
    )
)

import markdown_extensions

AUTHOR = 'Reilly Raab'
SITE_DESCRIPTION = (
    'This site is a space for me to share my interest in various subjects, ' +
    'publish personal essays, ' +
    'and communicate about projects or developments which are important to me.'
)
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

caching = True

###############################################################################
# PATHS

# content directory
# expected to have `articles` and `pages` subdirectories
PATH = 'content'
# additional subdirectories which are merely copied to output
STATIC_PATHS = ['images', 'hosted', 'js', 'css']
# File patterns which are ignored
IGNORE_FILES = ['.#*', '__pycache__']

# theme directory
# Expected to have `templates` and `static` subdirectories :(
THEME = 'theme'

# output directory
OUTPUT_PATH = 'public'

# path for plugins
PLUGIN_PATHS = ["plugins"]
# Plugin lists
PLUGINS = ["postprocess"]

# Caching
if caching:
    WITH_FUTURE_DATES = False
    CACHE_CONTENT = True
    LOAD_CONTENT_CACHE = True
    CACHE_PATH = 'cache'
    CHECK_MODIFIED_METHOD = 'md5'
    CONTENT_CACHING_LAYER = 'generator'

###############################################################################
# Optional Config

# write original file sources to output
OUTPUT_SOURCES = True

# Markdown settings
MARKDOWN = {
    'extensions': [
        markdown_extensions.Katex(),  # process math with katex
        markdown_extensions.Custom(),  # process math with katex
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
DRAFT_PAGE_SAVE_AS = '{slug}.html'

# Suppress Categories and Tags
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
FEEDS_SAVE_AS = ''

# These templates render directly as independent output
# DIRECT_TEMPLATES = ['index', 'links'] # 'links' lists all external links
DIRECT_TEMPLATES = ['index', 'private']

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
# REMOTE_FONT_URL = "https://fonts.googleapis.com/css?family=Roboto"

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
