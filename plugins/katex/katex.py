# -*- coding: utf-8 -*-
"""

Allow server-side KaTeX rendering for Markdown through node.js by registering
a Markdown extension with pelican.

The markdown extension adds regex patterns for `$` and `$$` in the source `.md`
file, and applies KaTeX to the intermediate text with a `python-bond` call to
node.js

requires
* node
* npm
* katex (npm install katex)
* python-bond (pip3 install --user python-bond)

KaTeX: https://github.com/Khan/KaTeX

Adapted from `render_math` plugin:
https://github.com/getpelican/pelican-plugins/tree/master/render_math

in turn adapted from:
https://github.com/barrysteyn/pelican_plugin-render_math

# Typogrify Compatibility

This plugin now plays nicely with Typogrify, but it
requires Typogrify version 2.07 or above.

"""

from distutils.version import LooseVersion

import markdown
from markdown.util import etree
from markdown.util import AtomicString

import bond

from pelican import signals, generators

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

class MathPattern(markdown.inlinepatterns.Pattern):

    def __init__(self, tag, pattern):
        super().__init__(pattern)
        self.tag = tag

    @independent_traceback
    def handleMatch(self, m):
        node = markdown.util.etree.Element(self.tag)
        node.set('class', 'math')

        orig = m.group('math')

        node.text = katex(orig, self.tag == 'div')

        return node

class MarkdownExtension(markdown.Extension):

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

# register our extension, and get it to play nice with other extensions
###############################################################################

def register():
    signals.initialized.connect(pelican_init)

def pelican_init(pelicanobj):
    # Register Markdown extension
    register_markdown_extension(pelicanobj)

    # Configure Typogrify
    configure_typogrify(pelicanobj)

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

@independent_traceback
def configure_typogrify(pelicanobj):
    """Instruct typogrify to ignore math and script tags"""

    if not pelicanobj.settings.get('TYPOGRIFY', False):
        return

    try:
        import typogrify

        if LooseVersion(typogrify.__version__) < LooseVersion('2.0.7'):
            raise TypeError('Typogrify version < 2.0.7')

        from typogrify.filters import typogrify

        pelicanobj.settings['TYPOGRIFY_IGNORE_TAGS'].extend(
            ['.math', 'script']
        )

    except (ImportError, TypeError) as e:
        # ImportError -> no typogrify
        # TypeError -> typogrify version < 2.0.7
        pelicanobj.settings['TYPOGRIFY'] = False
