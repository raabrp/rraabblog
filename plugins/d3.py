# -*- coding: utf-8 -*-
"""

Preprocessor for Markdown handling d3

 * Allow nicer way to make d3 charts (using /theme/static/js/charts.js)
   which offers some nice utilities.

How it happens:

 * We extend Markdown with a preprocessor which substitutes
   <d3> objects with <div> elements and the necessary Javascript
   boilerplate to use with charts.js

"""

import re
import json

from bs4 import BeautifulSoup

import markdown

class Preprocessor(markdown.preprocessors.Preprocessor):
    uid = 0

    def process_chunk(self, lines):

        node = BeautifulSoup('\n'.join(lines), 'html.parser').find()

        # parameters in the <d3> tag get passed to makeSVG function.
        params = {k.replace('-', '_'): v for k, v in node.attrs.items()}
        if not 'id' in params:
            params['id'] = 'd3_' + str(self.uid)
            self.uid += 1

        return [
            '<div id="{}" class="svg-container">'.format(params['id']),
            '<noscript>',
            '*JavaScript is not Enabled*',
            '</noscript>',
            '<script>',
            'onReady(function() {',
            'var svg = makeSVG({});'.format(
                json.dumps(params)
            ),
            '(function() {',
            *node.text.split('\n'),
            '}).call(svg);',
            '});',
            '</script>',
            '</div>'
        ]

    def run(self, lines):

        open_tag = re.compile('<d3')
        close_tag = re.compile('</d3>')

        def iterate_over(lines):

            for i, line in enumerate(lines):
                i = i
                open_match = open_tag.search(line)
                if open_match:
                    block_begin_index = i
                    partial_open = [line[open_match.start():]]
                    break
            else:
                return lines

            for i, line in enumerate(
                    partial_open + lines[block_begin_index + 1:]
            ):
                close_match = close_tag.search(line)
                if close_match:
                    block_close_index = i + block_begin_index
                    partial_close = [line[:close_match.end()]]
                    break
            else:
                raise ValueError(
                    'Incomplete tag at line {}'.format(block_begin_index)
                )

            internal_lines = self.process_chunk(
                partial_open +
                lines[block_begin_index:block_close_index] +
                partial_close
            )

            return (
                lines[:block_begin_index] +
                [lines[block_begin_index][:open_match.start()]] +
                internal_lines +
                [lines[block_close_index][close_match.end():]] +
                iterate_over(lines[block_close_index:])
            )

        return iterate_over(lines)

class D3_MD_Extension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        # uses preprocessor
        # https://github.com/lethain/python-markdown-graphviz/blob/master/mdx_graphviz.py
        # https://python-markdown.github.io/extensions/api/
        # https://alexwlchan.net/2017/03/extensions-in-python-markdown/

        md.preprocessors.add(
            'd3_element',
            Preprocessor(),
            '_begin'
        )
