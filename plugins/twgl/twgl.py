# -*- coding: utf-8 -*-
"""

What happens here:

 * Allow nicer way to make webgl shader animations (using twgl.js)
   which offers some nice utilities.

How it happens:

 * We extend Markdown with a preprocessor which substitutes
   <twgl> objects with <div> elements and the necessary Javascript
   boilerplate.

"""
import io
import sys
import traceback

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


class Preprocessor(markdown.preprocessors.Preprocessor):
    uid = 0

    def process_chunk(self, lines):

        node = BeautifulSoup('\n'.join(lines), 'html.parser').find()
        if not 'id' in params:
            params['id'] = 'd3_' + str(self.uid)
            self.uid += 1

        return [
            '<div id="{}-container" class="twgl-container">'.format(uid),
            '<noscript>',
            '*JavaScript is not Enabled*',
            '</noscript>',
            '<script id={} type="x-shader/x-fragment">'.format(uid),
            *node.text.split('\n'),
            '</script>',
            '<canvas id="{}_canvas"></canvas>'.format(uid),
            '<a id="{}_fsbind">View fullscreen</a>'.format(uid),
            '<script type="text/javascript">',
            'shade("{}");'.format(uid),
            '</script>',
            '</div>'
        ]

    @independent_traceback
    def run(self, lines):

        open_tag = re.compile('<twgl')
        close_tag = re.compile('</twgl>')

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
