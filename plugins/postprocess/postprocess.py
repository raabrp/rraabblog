'''

This file performs operations on the html content generated by pelican

What happens here:

* Estimate read time in minutes by number of words / WPM and assign as
  attribute `readtime` to articles and pages. Equations are included,
  but if anything, they should count for even more.

* Collect all links in metadata.

* Make Images have captions and links

* Make references better by setting 'title' attribute.

* Add some commented annotations to HTML source for debugging Katex math

'''

# assumed words per minute reading speed
WPM = 230.0 # http://en.wikipedia.org/wiki/Words_per_minute

import os
import re
import math
import datetime
import sys, traceback, io

from bs4 import BeautifulSoup

from urllib import parse as urlparse

from pelican import signals

from .encrypt import encrypt
from .d3 import d3
from .twgl import twgl
from .mol import molecule


BELL = '\u0007' # terminal bell

###############################################################################

def register():
    signals.content_object_init.connect(process_soup)

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

def parse_link(content_object, l):
    parsed_url = urlparse.urlparse(l.attrs['href'])

    return {
        'id': l.attrs['id'],
        'domain': '.'.join(parsed_url.netloc.split('.')[-2:]),
        'subdomain': '.'.join(parsed_url.netloc.split('.')[:-2]),
        'path': parsed_url.path.strip('/'),
        'text': l.text,
        'href': l.attrs['href'],
        'context': get_context_string(content_object, l),
        'article_title': content_object.title,
        'article_slug': content_object.slug,
    }

def get_context_string(content_object, target):
    prev_string = ''
    for node in target.previousGenerator():

        if node.name in ['li', 'ol', 'ul']:
            break

        if prev_string.count(BELL) > prev_string.endswith(BELL):
            break

        if isinstance(node, str) and not node.endswith('.org'):
            if node == '\n':
                prev_string = BELL + prev_string

            elif node.isdigit():
                continue

            else:
                prev_string = (
                    node
                    .replace('.', BELL)
                    .replace(':', BELL)
                    .replace(';', BELL)
                ) + prev_string

    # strip anything between '<' '>' pairs
    prev_string = re.sub('</?[^<>]*>', '', prev_string)

    if prev_string.endswith(BELL):
        prev_string = prev_string[:-1]

    # get last sentence and remove extra spaces
    return ' '.join(prev_string.split(BELL)[-1].split())

@independent_traceback
def process_soup(content_object):
    if content_object._content is None:
        return

    soup = BeautifulSoup(content_object._content, 'html.parser')

    # distinguish pages from projects
    setattr(content_object, 'project', (
        'projects' in content_object.source_path.split(os.sep)
    ))

    # last_updated formatting
    if hasattr(content_object, 'last_updated'):
        content_object.last_updated = datetime.datetime.strptime(
            content_object.last_updated, '%Y-%m-%d'
        )
    else:
        content_object.last_updated = content_object.date

    # estimate readtime
    content_object.readtime = {
        'minutes': math.ceil(len(soup.get_text().split()) / WPM)
    }

    a_id = 0
    # give links unique ids
    for l in soup.find_all('a'):
        if not 'id' in l.attrs:
            l.attrs['id'] = "generated-link-id" + str(a_id)
            a_id += 1

    # collect links as metadata
    all_links = [l for l in soup.find_all('a') if ('href' in l.attrs)]
    content_object.links = [
        parse_link(content_object, l) for l in all_links if any([
            l.attrs['href'].startswith('http'),
            l.attrs['href'].startswith('www')
        ])
    ]

    # make images better by allowing full screen interaction and caption
    img_id = 0
    for img in soup.find_all('img'):
        img_src = img.attrs['src']
        img_alt = img.attrs['alt']
        if not 'id' in img.attrs:
            img.attrs['id'] = "generated-img-id" + str(img_id)
            img_id += 0

        img.replaceWith(
            BeautifulSoup(
                img.decode() + '\n<p class="caption">' + img_alt + '</p>',
                'html.parser'
            )
        )

    # preview for Wikipedia links
    for a in soup.find_all('a'):
        if 'href' in a.attrs:
            if a.attrs['href'].startswith(
                    'https://en.wikipedia.org/wiki/'
            ):

                targetname = a.attrs['href'][len('https://en.wikipedia.org/wiki/'):]

                a.attrs['class'] = 'wikipedia_link'
                a.attrs['endpoint'] = \
                    'https://en.wikipedia.org/api/rest_v1/page/summary/{}'.format(
                        targetname
                    )

    # extract context of references to display as title attribute to backlinks
    for backref in soup.find_all(attrs={'class': 'footnote-backref'}):
        target = soup.find(attrs={'id': backref.attrs['href'].strip('#')})

        if not target:
            print(
                os.path.basename(content_object.source_path),
                'has an unused reference:',
                '"{}"'.format(backref.attrs['href'].strip('#fnref-'))
            )
            backref.extract()
            continue

        refcontext = get_context_string(content_object, target)
        if refcontext:
            backref.attrs['title'] = refcontext

    # prettify the math items
    for math_item in soup.find_all(attrs={'class': 'math'}):

        lvl = 0

        # white space must be respected, and getting around it with
        # comments for nice indentation looks ugly in the debugger
        transformed = math_item.decode()

        tex = math_item.find('annotation').get_text()

        math_item.replaceWith(BeautifulSoup(
            '\n<!--' + tex + '-->\n' + transformed + '\n',
            'html.parser')
        )

    # rainbow parentheses for codehilite
    for code in soup.find_all('div', {'class': 'codehilite'}):

        rainbow = 0

        for p in code.find_all('span', {'class': 'p'}):

            rep = ''

            for char in p.get_text():

                if char in '({[':
                    rainbow = (rainbow + 1) % 9
                    rep += '<span class="hlrb{0}">{1}</span>'.format(
                        rainbow,
                        char
                    )
                elif char in ')]}':
                    rep += '<span class="hlrb{0}">{1}</span>'.format(
                        rainbow,
                        char
                    )
                    rainbow = (rainbow - 1) % 9
                else:
                    rep += '<span class="p">{}</span>'.format(char)

            p.replaceWith(BeautifulSoup(rep, 'html.parser'))

    # d3
    d3(content_object, soup)

    # twgl
    twgl(content_object, soup)

    # molecule render molecules nicely
    molecule(content_object, soup)

    # inject script dependencies
    def attr_needs_scripts(attr, block):
        if hasattr(content_object, attr) and getattr(content_object, attr):
            injection = BeautifulSoup(block, 'html.parser')
            soup.contents.append(injection)

    attr_needs_scripts(
        'd3',
        """
<script src="theme/js/lib/d3.v5.min.js"></script>
<script src="theme/js/lib/simplify.js"></script>
<script src="theme/js/charts.js"></script>
<script src="theme/js/chart_components.js"></script>
"""
    )
    attr_needs_scripts(
        'speck',
        """
<script src="theme/js/lib/virtual-webgl.js"></script>
<script src="theme/js/lib/glMatrix.js"></script>
<script src="theme/js/lib/speck.js"></script>
"""
    )
    attr_needs_scripts(
        'twgl',
        """
<script src="theme/js/lib/twgl.min.js"></script>
<script src="theme/js/minshader.js"></script>
<script id="twgl_vs" type="x-shader/x-vertex">
 attribute vec4 position;

 void main() {
     gl_Position = position;
}
</script>
"""
    )

    # optionally password protect drafts
    if hasattr(content_object, 'password'):
        encrypt(content_object, soup)
    else:
        content_object._content = soup.decode()
