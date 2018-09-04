# -*- coding: utf-8 -*-
"""

What happens here:

 * Allow nicer way to make d3 charts (using /theme/static/js/charts.js)
   which offers some nice utilities.

TODO
 * Allow use of mathbox

TODO
 * Allow server-side pre-rendering of animations to webm.

How it happens:

 * We extend Markdown with a preprocessor which substitutes
   <d3> objects with <div> elements and the necessary Javascript
   boilerplate to use with charts.js

TODO
 * Allow us to use node to generate the svg server-side and display the static
   SVG if d3 cannot be loaded client-side - or better yet - render to looping
   webm formats.
   - See katex plugin implementation with bond and jsdom

Note:
Re-rendering SVGs for each frame with d3 can be too CPU intensive when actually
modifying the DOM. In such cases, go with Mathbox instead or render to webm.

DoubleNote:
With integrated graphics, I incur about the same CPU load for painting a simple
wiggling line with either library. :(

d3 is good for: interactivity, colors.
mathbox is good for: leveragiing gpu

"""
import io
import sys
import traceback
import uuid

import re
import json

from bs4 import BeautifulSoup

import markdown
from markdown.util import etree
from markdown.util import AtomicString

import bond

from pelican import signals, generators

def independent_traceback(func):
    '''
    Pelican suppresses tracebacks, so we print them to stdout
    '''
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            with io.StringIO() as mock_stdout:
                traceback.print_exception(*sys.exc_info(), file=mock_stdout)
                sys.stderr.write(mock_stdout.getvalue())
                raise e
    return wrapped

###############################################################################

# JS = bond.make_bond('JavaScript')
# JS.eval_block(
#     r'''
#     var d3 = require("d3");
#     const jsdom = require("jsdom");
#     const { JSDOM } = jsdom;

#     function render(s, is_block) {
#       return ???;
#     }
#     '''
# )
# render_svg = JS.callable('render')

class Preprocessor(markdown.preprocessors.Preprocessor):

    def process_chunk(self, lines):

        node = BeautifulSoup('\n'.join(lines), 'html.parser').find()

        # parameters in the <d3> tag get passed to makeSVG function.
        params = {k.replace('-', '_'): v for k, v in node.attrs.items()}
        if not 'id' in params:
            params['id'] = uuid.uuid1().hex

        return [
            '<div id="{}" class="svg-container">'.format(params['id']),
            '<noscript>',
            '*JavaScript is not Enabled*',
            '</noscript>',
            '</div>',
            '<div>',
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

    @independent_traceback
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

class MarkdownExtension(markdown.Extension):

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

# register our extension, and get it to play nice with other extensions
###############################################################################

def register():
    signals.initialized.connect(pelican_init)

def pelican_init(pelicanobj):
    # Register Markdown extension
    register_markdown_extension(pelicanobj)

@independent_traceback
def register_markdown_extension(pelicanobj):
    """
    place the markdown extension object at the correct place in the settings
    """

    markdown_extension = MarkdownExtension()

    if 'MARKDOWN' in pelicanobj.settings:
        if 'extensions' in pelicanobj.settings['MARKDOWN']:
            pelicanobj.settings['MARKDOWN']['extensions'].append(
                markdown_extension
            )
        else:
            pelicanobj.settings['MARKDOWN']['extensions'] = [
                markdown_extension
            ]
    elif 'MD_EXTENSIONS' in pelicanobj.settings:
        pelicanobj.settings['MD_EXTENSIONS'].append(
            markdown_extension
        )
    else:
        raise LookupError("Could not find pelicanobj.settings['MARKDOWN']")
