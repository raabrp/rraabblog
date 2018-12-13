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
import json
import markdown

AUTHOR = 'Reilly Raab'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

# Input/Output/Template Paths
_DIR = os.path.dirname(os.path.realpath(__file__))
THEME = os.path.join(_DIR, 'theme')
PATH = os.path.join(_DIR, 'content')
STATIC_PATHS = ['images', 'static', 'js', 'css']
IGNORE_FILES = ['.#*', '__pycache__']
OUTPUT_PATH = os.path.join(_DIR, 'public')
PLUGIN_PATHS = ["plugins"]
OUTPUT_SOURCES = True

# Plugin lists
PLUGINS = ["soup", "katex", "d3"]

# Markdown settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {
            'permalink': '#'
        },
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.smarty': {
            'smart_angled_quotes': True
        },
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Third party fonts
REMOTE_FONT_URL = "https://fonts.googleapis.com/css?family=Raleway:600i|Roboto"

# URL patterns
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DRAFT_SAVE_AS = '{slug}.html'
SLUGIFY_SOURCE = 'slug'

# Suppress Categories and Tags
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
FEEDS_SAVE_AS = ''

# Suppress other extraneous pages
DIRECT_TEMPLATES = ['index', 'links']

# Suppress other unnecessary utilities
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
LINKS = None
SOCIAL = None
DEFAULT_PAGINATION = False

# Allow definition of variables using python which will be available
# to Jinja theme templates or javascript files
###############################################################################

# theme names
color_prefix = "color-"
color_suffix = ".css"
theme_names = sorted([
    x[len(color_prefix):-len(color_suffix)] for x in \
    os.listdir(os.path.join(THEME, 'static', 'css')) \
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

###############################################################################
