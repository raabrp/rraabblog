"""Render D3"""

import json
from bs4 import BeautifulSoup

def d3(content_object, soup):

    d3_id = 0
    for d3 in soup.find_all('d3'):

        content_object.d3 = True

        params = {k.replace('-', '_'): v for k, v in d3.attrs.items()}

        if not 'id' in params:
            params['id'] = "generated-d3-id" + str(d3_id)
            d3_id += 1

        d3.replaceWith(
            BeautifulSoup("""
<div id="{id}" class="svg-container">
    <noscript>JavaScript is not Enabled</noscript>
    <script>
        onReady(function() {{
            var svg = makeSVG({params});

            (function() {{
                {content}
            }}).call(svg);
        }});
    </script>
</div>""".format(
    id=params['id'],
    params=json.dumps(params),
    content=d3.get_text()
),
                'html.parser'
            )
        )
