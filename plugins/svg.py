# -*- coding: utf-8 -*-
"""

Preprocessor for Inlining svg

 * We extend Markdown with a preprocessor which substitutes
   <inlinesvg> objects with <svg> elements

"""

import re

from bs4 import BeautifulSoup

import markdown

class Preprocessor(markdown.preprocessors.Preprocessor):

    def process_chunk(self, lines):

        node = BeautifulSoup('\n'.join(lines), 'lxml-xml').find()

        # parameters in the <inlinesvg> tag get passed to makeSVG function.
        params = {k.replace('-', '_'): v for k, v in node.attrs.items()}
        print('#####')
        print()
        print(params)
        print()
        print('#####')

        # with open(params['src']) as f:
        #     content = BeautifulSoup(f.read(), 'lxml-xml')

        # content.decode()

        return []

    def run(self, lines):

        open_tag = re.compile('<inlinesvg')
        close_tag = re.compile('</inlinesvg>')

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

class SVG_MD_Extension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):

        md.preprocessors.add(
            'inlinesvg_element',
            Preprocessor(),
            '_begin'
        )
