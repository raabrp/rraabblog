# -*- coding: utf-8 -*-
"""

Preprocessor for Markdown handling d3

 * Allow Macros!
 * Allow nicer way to make d3 charts (using /theme/static/js/charts.js)
   which offers some nice utilities.

How it happens:

 * We extend Markdown with a preprocessor which substitutes
   <d3> objects with <div> elements and the necessary Javascript
   boilerplate to use with charts.js

"""

import re
import json
import time
import datetime

from bs4 import BeautifulSoup

import markdown

class Preprocessor(markdown.preprocessors.Preprocessor):

    def run(self, lines):

        start = time.time()

        processed = []

        unwrap = False

        # wrap script, div, and twgl tags in div tags
        for line in lines:

            line = line.replace(
                '<d3',
                '<div><d3'
            ).replace(
                '</d3>',
                '</d3></div>'
            ).replace(
                '<twgl',
                '<div><twgl'
            ).replace(
                '</twgl>',
                '</twgl></div>'
            ).replace(
                '<script',
                '<div><script'
            ).replace(
                '</script>',
                '</script></div>'
            )

            setunwrap = line.endswith('\\')
            if not unwrap:
                if not setunwrap:
                    processed.append(line)
                else:
                    processed.append(line[:-1])
            else:
                if not setunwrap:
                    processed[-1] = processed[-1] + line
                else:
                    processed[-1] = processed[-1] + line[:-1]
            unwrap = setunwrap

        print(datetime.datetime.now().strftime("%H:%M:%S.%f"), round(time.time() - start, 2), "seconds in preprocessing")
        return processed

class Custom(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        # uses preprocessor
        # https://github.com/lethain/python-markdown-graphviz/blob/master/mdx_graphviz.py
        # https://python-markdown.github.io/extensions/api/
        # https://alexwlchan.net/2017/03/extensions-in-python-markdown/

        md.preprocessors.add(
            '_custom',
            Preprocessor(),
            '_begin'
        )
