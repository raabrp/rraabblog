# -*- coding: utf-8 -*-
"""

Allow server-side KaTeX rendering for Markdown through node.js

The markdown extension adds regex patterns for `$` and `$$` in the source `.md`
file, and applies KaTeX to the intermediate text with a `python-bond` call to
node.js

requires
* node
* npm
* katex (npm install katex)
* python-bond (pip3 install --user python-bond)

KaTeX: https://github.com/Khan/KaTeX

"""


import markdown
from markdown.util import etree

import bond

JS = bond.make_bond('JavaScript')
JS.eval_block(
    r'''
    katex = require('katex');
    function render(s, is_block) {
      return katex.renderToString(s, { displayMode: is_block });
    }
    '''
)
katex = JS.callable('render')

###############################################################################

class MathPattern(markdown.inlinepatterns.Pattern):

    def __init__(self, tag, pattern):
        super().__init__(pattern)
        self.tag = tag

    def handleMatch(self, m):
        node = markdown.util.etree.Element(self.tag)
        node.set('class', 'math')

        orig = m.group('math')

        node.text = katex(orig, self.tag == 'div')

        return node

class Katex_MD_Extension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):

        # Regex to detect math delimiters
        math_inline_regex = \
            r'(?P<prefix>\$)(?P<math>.+?)(?P<suffix>(?<!\s)\2)'
        math_block_regex = \
            r'(?P<prefix>\$\$|\\begin\{(.+?)\})(?P<math>.+?)(?P<suffix>\2|\\end\{\3\})'

        # Process math before escapes are processed since escape processing
        # will interfere. The order in which the displayed and inlined math
        # is registered below matters
        md.inlinePatterns.add(
            'math_block',
            MathPattern('div', math_block_regex),
            '<escape'
        )
        md.inlinePatterns.add(
            'math_inline',
            MathPattern('span', math_inline_regex),
            '<escape'
        )
