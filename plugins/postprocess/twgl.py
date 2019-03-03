"""Render TWGL"""

from bs4 import BeautifulSoup

def twgl(content_object, soup):

    twgl_id = 0
    for twgl in soup.find_all('twgl'):

        content_object.twgl = True

        params = {k.replace('-', '_'): v for k, v in twgl.attrs.items()}

        if not 'id' in params:
            params['id'] = 'generated-twgl-id' + str(twgl_id)
            twgl_id += 1

        if not 'vs' in params:
            params['vs'] = "twgl_vs"

        twgl.replaceWith(
            BeautifulSoup("""
<div id="{id}-container" class="twgl-container">
    <noscript>JavaScript is not Enabled</noscript>
    <script id={id}_shader type="x-shader/x-fragment">
        {content}
    </script>
    <canvas id="{id}_canvas"></canvas>
    <a id="{id}_fs">View fullscreen</a>
    <script type="text/javascript">
        onReady(function() {{
            {id}_obj = new shade("{id}", "{vs}");
        }});
    </script>
</div>
""".format(
    id=params['id'],
    vs=params['vs'],
    content=twgl.get_text()
),
                          'html.parser'
            )
        )
