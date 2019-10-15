"""Render chemicals in 3D"""

from bs4 import BeautifulSoup

from .dict_replace import dict_replace

def molecule(content_object, soup):
    '''
    works through side-effects to content_object and soup
    '''

    for mol in soup.find_all('mol'):

        mol.replaceWith(BeautifulSoup("""
<table>
 <tr>
  <td>
   <chemsvg class="mol" src="{svg}" />
  </td>
  <td>
   <speck src="{xyz}"></speck>
  </td>
 </tr>
</table>
""".format(svg=mol.attrs['svg'], xyz=mol.attrs['xyz']),
        'html.parser')
        )

    # inlinesvg
    isvg_id = 0
    for isvg in soup.find_all('chemsvg'):
        if not 'id' in isvg.attrs:
            isvg.attrs['id'] = "generated-isvg-id" + str(isvg_id)
            isvg_id += 1

        img_src = isvg.attrs['src']

        with open(img_src) as f:
            content = f.read()

        def molcolormap(x):
            '''
            x = [
                ["rgb(0, 0, 0)", "rgb(1, 1, 1)", "rbga(1, 1, 1, 1)"]
                ...
            ]
            '''
            mapdict = {
                # condense
                '\n': '',
                'fill="none"': '',
                'paint-order="fill stroke markers"': '',
                'stroke-dasharray=""': '',
                'stroke-linejoin="round"': '',
                'stroke-miterlimit="10"': '',
                'font-style="normal"': '',
                'font-weight="normal"': '',
                'stroke="none"': '',
                'text-anchor="start"': '',
                'text-decoration="normal"': '',
                'dominant-baseline="alphabetic"': '',
                'font-family="sans-serif"': '',
                # change attributes
                'rgb(0,0,0)': 'var(--w0)',
                'stroke-width="1.5"': 'stroke-width="2"',
                'font-size="12px"': 'font-size="18px"',
                'font-size="8px"': 'font-size="12px"',
                'fill="white"': 'fill="none"',
                'Tb': 'R',
                # round numbers
                '\\d+\\.\\d+': lambda x: str(round(float(x), 1)),
            }
            # Change colors
            for k, v, a in x:
                mapdict['fill="{}"'.format(k)] = \
                    'fill="{}"'.format(v)
                mapdict['offset="0" stop-color="{}"'.format(k)] = \
                    'offset="0" stop-color="{}"'.format(a)
                mapdict['offset="0.45" stop-color="{}"'.format(k)] = \
                    'offset="0.45" stop-color="{}"'.format(v)
                mapdict['offset="0.55" stop-color="{}"'.format(k)] = \
                    'offset="0.55" stop-color="{}"'.format(v)
                mapdict['offset="1" stop-color="{}"'.format(k)] = \
                    'offset="1" stop-color="{}"'.format(a)
            return mapdict

        if content.startswith("<!-- processed -->"):
            s = BeautifulSoup(content, 'html.parser')
        else:

            s = BeautifulSoup(
                dict_replace(
                    content,
                    molcolormap([
                        # H
                        ['rgb(100,100,100)', 'var(--w0)', 'var(--w0_)'],
                        # Tb
                        ['rgb(0,153,0)', 'rgb(255,20,147)', 'rgba(255,20,147,0)'],
                        # N
                        ['rgb(51,51,153)', 'rgb(48,80,248)', 'rgba(48,80,248,0)'],
                        # O
                        ['rgb(255,0,0)', 'rgb(255,13,13)', 'rgba(255,13,13,0)'],
                        # P
                        ['rgb(153,102,0)', 'rgb(255,128,0)', 'rgba(255,128,0,0)'],
                        # Br
                        ['rgb(102,51,51)', 'rgb(166,41,41)', 'rgba(166,41,41,0)'],
                        # S
                        ['rgb(102,102,0)', 'rgb(166,166,20)', 'rgba(166,166,20,0)']
                    ])
                ),
                'html.parser'
            )

            h_atoms = []
            nh_atoms = []
            nums = []

            for text in s.find_all('text'):
                if text.text == 'H':
                    text.attrs['fill'] = 'var(--w0)'
                    h_atoms.append(text)
                elif text.text.isdigit():
                    nums.append(text)
                else:
                    nh_atoms.append(text)

            # Shift H Labels
            for h_atom in h_atoms:

                hx = float(h_atom.attrs['x'])
                hy = float(h_atom.attrs['y'])

                for nh in nh_atoms:
                    nx = float(nh.attrs['x'])
                    ny = float(nh.attrs['y'])

                    if ((nx - hx) ** 2 + (ny - hy) ** 2) < 400:
                        shift = [(hx - nx) * 1.3, (hy - ny) * 1.5]
                        h_atom.attrs['x'] = str(nx + shift[0])
                        h_atom.attrs['y'] = str(ny + shift[1])
                        break

                # Shift numbers
                for num in nums:
                    nx = float(num.attrs['x'])
                    ny = float(num.attrs['y'])

                    if ((nx - hx) ** 2 + (ny - hy) ** 2) < 400:

                        num.attrs['fill'] = 'var(--w0)'
                        shift = [(nx - hx) * 1.3, (ny - hy) * 1.5]
                        hx = float(h_atom.attrs['x'])
                        hy = float(h_atom.attrs['y'])
                        num.attrs['x'] = str(hx + shift[0])
                        num.attrs['y'] = str(hy + shift[1])
                        break

            # Shift R labels
            for text in s.find_all('text'):
                text.attrs['y'] = str(float(text.attrs['y']) + 2)

                # Shift all other atoms
                if text.text == 'O': # 'O' is wider
                    text.attrs['x'] = str(float(text.attrs['x']) - 1.5)

                elif text.text == 'R': # was spaced for 'Tb'
                    text.attrs['x'] = str(float(text.attrs['x']) + 1.3)

                else: # H, P, N, etc
                    text.attrs['x'] = str(float(text.attrs['x']) - 2)

            # with open(img_src, 'w') as f:
            #    f.write("<!-- processed -->" + s.decode())

        r = s.find('svg')
        r.attrs['id'] = isvg.attrs['id']

        w = h = None
        if 'width' in r.attrs:
            w = float(r.attrs['width'])
            del(r.attrs['width'])
        if 'height' in r.attrs:
            h = float(r.attrs['height'])
            del(r.attrs['height'])

        if w and h:
            r.attrs['viewbox'] = "-20 -20 {} {}".format(w + 40, h + 40)

        if 'class' in isvg.attrs:
            r.attrs['class'] = isvg.attrs['class'].append('inlinesvg')
        else:
            r.attrs['class'] = 'inlinesvg'

        isvg.replaceWith(s)

    # speck
    speck_id = 0
    for speck in soup.find_all('speck'):
        xyz_src = speck.attrs['src']

        content_object.speck = True

        if not 'id' in speck.attrs:
            speck.attrs['id'] = "generated-speck-id" + str(speck_id)
            speck_id += 1

        with open(xyz_src) as f:
            content = f.read()

        s = BeautifulSoup("""
<div style="width: 300px; height: 300px;">
<canvas width="768px" height="768px" id="{0}" class="speck-canvas"></canvas>
<noscript>
*JavaScript is not Enabled*
</noscript>
<script type="text/javascript">
    onReady(function() {{
        var speck;
        speck = Speck.new("{0}",
`{data}`);
        bindScrollTriggers(
            document.getElementById("{0}"),
            function() {{
                addAnimation(speck.render);
            }},
            function() {{
                removeAnimation(speck.render);
            }}
        );
    }});
</script>
</div>
        """.format(speck.attrs['id'], data=content),
        'html.parser')

        speck.replaceWith(s)
