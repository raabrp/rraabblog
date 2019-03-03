---
title: Encryption Demo
slug: encrypted
password: encrypted
date: 2018-01-01
---

<h2>(Demonstration of encrypted content)</h2>

***

[TOC]


# Article Meta

The top of this file includes

```
---
title: Encryption Demo
slug: encrypted
password: encrypted
date: 2018-01-01
---

[TOC]

```

| Line       | Explanation                                               |
|------------|-----------------------------------------------------------|
| `title`    | Appears at top of page and title of browser tab           |
| `slug`     | Path of generated html file relative to website root      |
| `password` | Password to decrypt generated page                        |
| `date`     | Date shown at top and sorted by on index page             |
| `[TOC]`    | Generates Table of Contents (at this location for mobile) |

Note that encrypted pages are not linked from the index page, nor is the
unprocessed source copied to the public directory.

# Header 1

## Header 2

### Header 3

#### Header 4


```
# Header 1

## Header 2

### Header 3

#### Header 4
```

# Plain text

This is plain text ... with – ｕｎｉｃｏｄｅ – 👍 and HTML escape sequences&#33;

Two line breaks start a new paragraph.

```
This is plain text ... with – ｕｎｉｃｏｄｅ – 👍 and HTML escape sequences&#33;

Two line breaks start a new paragraph.
```

# Links

Link to an [example](http://www.example.com) domain

```
Link to an [example](http://www.example.com) domain
```

Links to [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia) pages will
display summaries when hovered over.

```
Links to [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia) pages will
display summaries when hovered over.
```

# Text Decoration

Text decoration may include *italicized text*, _alternate italicized text_,
**bold text**, __alternate bold text__, `monospace text`, **_nested_ text
decorations**, and standard HTML<sup>when&nbsp;necessary<sub>.

```
Text decoration may include *italicized text*, _alternate italicized text_,
**bold text**, __alternate bold text__, `monospace text`, **_nested_ text
decorations**, and standard HTML<sup>when&nbsp;necessary<sub>.
```

# Block Quotes


> There was only one catch and that was Catch-22, which specified that a concern
> for one's own safety in the face of dangers that were real and immediate was 
> the process of a rational mind. Orr was crazy and could be grounded. All he 
> had to do was ask; and as soon as he did, he would no longer be crazy and 
> would have to fly more missions.
>
> -- Joseph Heller, Catch-22 (1961)

```
> There was only one catch and that was Catch-22, which specified that a concern
> for one's own safety in the face of dangers that were real and immediate was 
> the process of a rational mind. Orr was crazy and could be grounded. All he 
> had to do was ask; and as soon as he did, he would no longer be crazy and 
> would have to fly more missions.
>
> -- Joseph Heller, Catch-22 (1961)
```

# Footnotes

A provocative or dubious claim is well served by a footnote, which will be
placed at the bottom of the page.[^unique string] The link representing the
footnote may be hovered over to show the footnote or clicked to scroll to it.

[^unique string]: You may source or comment upon your claims within footnotes,
embedding external references as appropriate
<<[example.com](https://www.example.com)>>. A user may hover over the ↩ icon
next to the footnote to see the context surrounding its usage and click it to
return to that location in the article.

```
A provocative or dubious claim is well served by a footnote, which will be
placed at the bottom of the page.[^unique string] The link representing the
footnote may be hovered over to show the footnote or clicked to scroll to it.

[^unique string]: You may source or comment upon your claims within footnotes,
embedding external references as appropriate
<<[example.com](https://www.example.com)>>. A user may hover over the ↩ icon
next to the footnote to see the context surrounding its usage and click it to
return to that location in the article.
```

If you leave a space between a sentence and a footnote, no context will be given
by the `title` attribute of the ↩ return link. [^nocontext]

[^nocontext]: This footnote will not display its context when the ↩ icon is
hovered over.

```
If you leave a space between a sentence and a footnote, no context will be given
by the `title` attribute of the ↩ return link. [^nocontext]

[^nocontext]: This footnote will not display its context when the ↩ icon is
hovered over.
```

# Images

![Recursive Landscape. Courtesy of 
<a href="https://imgur.com/tos">Imgur</a>](/images/RecursiveLandscape.gif)

```
![Recursive Landscape. Courtesy of 
<a href="https://imgur.com/tos">Imgur</a>](/images/RecursiveLandscape.gif)
```

Clicking on an image will make it fullscreen.

# Horizontal Rule

Text above the line.

***

Text below the line.

```
Text above the line.

***

Text below the line.
```

# Lists and Bullets

1. The first list item determines it's type (numbered or unordered)
+ Other bullets can be numbers, `+`, `-`, or `*`
     * Sublists may be ordered or unordered

     <!-- two newlines and other content (e.g. a comment) divides list types -->
     1. Ordered sub-list

     You can have properly indented paragraphs within list items.

     Merely indent content by 4 spaces, as you do with sublists.
     
- Continuation of the first list
* Last item
   
<!-- Comment again used to divide lists types -->
   
* First item determines its type (this list is unordered)
1. Even if later items are digits
    * Sub item
        * sub-sub item
            * sub-sub-sub item
            
```
1. The first list item determines it's type (numbered or unordered)
+ Other bullets can be numbers, `+`, `-`, or `*`
     * Sublists may be ordered or unordered

     <!-- two newlines and other content (e.g. a comment) divides list types -->
     1. Ordered sub-list

     You can have properly indented paragraphs within list items.

     Merely indent content by 4 spaces, as you do with sublists.
     
- Continuation of the first list
* Last item
   
<!-- Comment again used to divide lists types -->
   
* First item determines its type (this list is unordered)
1. Even if later items are digits
    * Sub item
        * sub-sub item
            * sub-sub-sub item
```

# Tables

| Sepal.Length | Sepal.Width | Petal.Length | Petal.Width | Species |
|-------------:|------------:|-------------:|------------:|:--------|
|          5.1 |         3.5 |          1.4 |         0.2 | setosa  |
|          4.9 |         3.0 |          1.4 |         0.2 | setosa  |
|          4.7 |         3.2 |          1.3 |         0.2 | setosa  |
|          4.6 |         3.1 |          1.5 |         0.2 | setosa  |
|          5.0 |         3.6 |          1.4 |         0.2 | setosa  |
|          5.4 |         3.9 |          1.7 |         0.4 | setosa  |


```
| Sepal.Length | Sepal.Width | Petal.Length | Petal.Width | Species |
|--------------|-------------|--------------|-------------|---------|
|          5.1 |         3.5 |          1.4 |         0.2 | setosa  |
|          4.9 |         3.0 |          1.4 |         0.2 | setosa  |
|          4.7 |         3.2 |          1.3 |         0.2 | setosa  |
|          4.6 |         3.1 |          1.5 |         0.2 | setosa  |
|          5.0 |         3.6 |          1.4 |         0.2 | setosa  |
|          5.4 |         3.9 |          1.7 |         0.4 | setosa  |
```

# Comments

Prior to comment. <!-- This is a comment --> After comment.

~~~
Prior to comment. <!-- This is a comment --> After comment.
~~~

# Injected HTML / Javascript

<div id="example"></div>
<script type="text/javascript">
document.getElementById("example").innerHTML="Hello, world!";
</script>

<!-- there is a zero-width non-breaking space after the `<` in the `<(\)script>`
     tags below -->
     
~~~html
<div id="example"></div>
<script type="text/javascript">
    document.getElementById("example").innerHTML="Hello, world!";
</script>
~~~

Note: the `<div>` tag wrapping the `<​script>` tag is not necessary; it is
inserted by the preprocessor.

# Math (KaTeX)

Using [$\KaTeX$](https://katex.org)

Use `$` to wrap inline math:

As $x \to \infty$, $(1 - \frac{1}{x})^{x}$ approaches $\frac{1}{e}$.

```
As $x \to \infty$, $(1 - \frac{1}{x})^{x}$ approaches $\frac{1}{e}$.
```

Use `$$` to wrap multi-line expressions:

$$
\forall \delta \in X^Y,
\frac{\partial}{\partial \varepsilon}
\int_X ~ L ( 
f^\dagger + \varepsilon \delta, 
f^\dagger_x + \varepsilon \delta_x,
x 
) ~ dx = 0
$$

```
$$
\forall \delta \in X^Y,
\frac{\partial}{\partial \varepsilon}
\int_X ~ L ( 
f^\dagger + \varepsilon \delta, 
f^\dagger_x + \varepsilon \delta_x,
x 
) ~ dx = 0
$$
```

# Syntax Highlighting

Syntax highlighting uses [pygments](http://pygments.org/languages/) via
[codehilite](https://python-markdown.github.io/extensions/code_hilite/#syntax),
with post-processing for rainbow parentheses.

Lines may be highlighted (here lines 4 and 8 are)

```{.python hl_lines='4 8'}
import numpy as np

@decorator
def foo(x, y):
    '''Docstring for foo'''
    if boolean_expression is True:
        print('condition met') # inline comment
    z = x + y
    return z + 0

class MyClass:
    pass
```

~~~html
```python hl_lines='4 8'

import numpy as np

@decorator
def foo(x, y):
    '''Docstring for foo'''
    if boolean_expression is True:
        print('condition met') # inline comment
    return x + y + 0

class MyClass:
    pass
```
~~~

Indent blocks with a shebang specifying language for line numbers

    #!javascript
    
    // Comment
    window.onload = function() { 
        for (var i = 0; i < 100; i++) {
            alert('Hello World!');
        }
    };

```md
    #!javascript
    
    // Comment
    window.onload = function() { 
        for (var i = 0; i < 100; i++) {
            alert('Hello World!');
        }
    };
```

Note, each of these:

* `<code>source code</code>`
* <code>\`\`\`source code\`\`\`</code>
* `~~~source code~~~`
* `source code indented by 4 spaces`
 
will wrap the resulting HTML in `code` tags, though nesting can create
difficulties, and specifying a language cannot be done with each method.

# Reusable D3 Charts

I'm still working out how to do charting most effectively. 
[Mathbox](https://acko.net/blog/mathbox2/) is high on the todo list for this
purpose, but I'm more familiar with D3. This is mostly a proof-of-concept at the
moment, but may be extended upon in the future.

By default, only content in view is rendered or animated. Animations are
parametric, as are some components (see the line below, which uses adaptive
resampling by default).

<d3 height="50">

/*
 * Uses components Line and Text from `theme/static/js/chart_components.js`
 * See `theme/static/js/charts.js`
 * See `plugins/charts/d3.py`
 */
 
this.attach_component(Line, 'someline')
    .use(function(selection) {
        selection.attr("style", function(d) { 
            return "stroke:" + d.color + "; fill: none;";
        });
    });

this.attach_component(Text, 'arclength_label')
    .transform(250, 0)
    .use(function(selection) {
        selection.attr("style", function(d) {
            return "fill:" + d.color + ";";
        });
    });

this.attach_component(Text, 'mode1_label')
    .transform(250, 20)
    .use(function(selection) {
        selection.attr("style", function(d) {
            return "fill:" + d.color + ";";
        });
    });
    
this.attach_component(Text, 'mode2_label')
    .transform(250, 40)
    .use(function(selection) {
        selection.attr("style", function(d) {
            return "fill:" + d.color + ";";
        });
    });

this.attach_component(Text, 'mode3_label')
    .transform(250, 60)
    .use(function(selection) {
        selection.attr("style", function(d) {
            return "fill:" + d.color + ";";
        });
    });

this.animate_periodic_with(200, function(p) {
  /*
   * the first parameter of animate_periodic_with is the number of 
   * frames per period.
   *
   * the second is a function of p, where p is in domain [0, 1),
   * corresponding to one period of animation
   */
 
  const num_points = 100;
  const width = 200;
  const amp = 25;
  const min_arc_length = width;
  const Tau = 2 * Math.PI;

  var mode1_c = Math.sin(Tau * p + .1) * 0.3;
  var mode2_c = Math.sin(Tau * p * 2 + .2) * 0.2;
  var mode3_c = Math.sin(Tau * p * 3 - .1) * 0.2;
  
  // is closure with respect to p
  function parameterized(s) {
    return {
      x: width * s,
      y: amp * (
        Math.sin(Tau * s ) * mode1_c - 
        Math.sin(Tau * s * 2) * mode2_c + 
        Math.sin(Tau * s * 3) * mode3_c
      ) + amp
    };
  }
  
  var pts = new Array(num_points);
  var arc_length = 0;
  
  for (var i = 0; i < num_points; i++) {
    pts[i] = parameterized(i / (num_points - 1));
  }
  // integrate to compute arc length
  for (var i = 0; i < num_points - 1; i++) {
    arc_length += Math.sqrt(
      (pts[i].x - pts[i + 1].x) ** 2 + 
      (pts[i].y - pts[i + 1].y) ** 2
    )
  }
  
  return {
      someline: {
          points: pts,
          color: "var(--w0)"
      },
      arclength_label: {
          color: "var(--w0)",
          value: "Arclength: " + (arc_length / min_arc_length)
                                  .toFixed(2).toString()
      },
      mode1_label: {
          color: "var(--w0)",
          value: "Mode 0 Coefficient: " + mode1_c.toFixed(2).toString()
      },
      mode2_label: {
          color: "var(--w0)",
          value: "Mode 1 Coefficient: " + mode2_c.toFixed(2).toString()
      },
      mode3_label: {
          color: "var(--w0)",
          value: "Mode 2 Coefficient: " + mode3_c.toFixed(2).toString()
      }
  };
});

</d3>

The animation routines for the d3 svg will run only when scrolled into view.

<!-- there is a zero-width non-breaking space following the `<` in the `<(\)d3>`
     tags below -->
     
```javascript
<​d3 height="50">

/*
 * Uses components Line and Text from `theme/static/js/chart_components.js`
 * See `theme/static/js/charts.js`
 * See `plugins/charts/d3.py`
 */
 
this.attach_component(Line, 'someline')
    .use(function(selection) {
        selection.attr("style", function(d) { 
            return "stroke:" + d.color + "; fill: none;";
        });
    });

this.attach_component(Text, 'arclength_label')
    .transform(250, 0)
    .use(function(selection) {
        selection.attr("style", function(d) {
            return "fill:" + d.color + ";";
        });
    });

this.attach_component(Text, 'mode1_label')
    .transform(250, 20)
    .use(function(selection) {
        selection.attr("style", function(d) {
            return "fill:" + d.color + ";";
        });
    });
    
this.attach_component(Text, 'mode2_label')
    .transform(250, 40)
    .use(function(selection) {
        selection.attr("style", function(d) {
            return "fill:" + d.color + ";";
        });
    });

this.attach_component(Text, 'mode3_label')
    .transform(250, 60)
    .use(function(selection) {
        selection.attr("style", function(d) {
            return "fill:" + d.color + ";";
        });
    });

this.animate_periodic_with(200, function(p) {
  /*
   * the first parameter of animate_periodic_with is the number of 
   * frames per period.
   *
   * the second is a function of p, where p is in domain [0, 1),
   * corresponding to one period of animation
   */
 
  const num_points = 100;
  const width = 200;
  const amp = 25;
  const min_arc_length = width;
  const Tau = 2 * Math.PI;

  var mode1_c = Math.sin(Tau * p + .1) * 0.3;
  var mode2_c = Math.sin(Tau * p * 2 + .2) * 0.2;
  var mode3_c = Math.sin(Tau * p * 3 - .1) * 0.2;
  
  // is closure with respect to p
  function parameterized(s) {
    return {
      x: width * s,
      y: amp * (
        Math.sin(Tau * s ) * mode1_c - 
        Math.sin(Tau * s * 2) * mode2_c + 
        Math.sin(Tau * s * 3) * mode3_c
      ) + amp
    };
  }
  
  var pts = new Array(num_points);
  var arc_length = 0;
  
  for (var i = 0; i < num_points; i++) {
    pts[i] = parameterized(i / (num_points - 1));
  }
  // integrate to compute arc length
  for (var i = 0; i < num_points - 1; i++) {
    arc_length += Math.sqrt(
      (pts[i].x - pts[i + 1].x) ** 2 + 
      (pts[i].y - pts[i + 1].y) ** 2
    )
  }
  
  return {
      someline: {
          points: pts,
          color: "var(--w0)"
      },
      arclength_label: {
          color: "var(--w0)",
          value: "Arclength: " + (arc_length / min_arc_length)
                                  .toFixed(2).toString()
      },
      mode1_label: {
          color: "var(--w0)",
          value: "Mode 0 Coefficient: " + mode1_c.toFixed(2).toString()
      },
      mode2_label: {
          color: "var(--w0)",
          value: "Mode 1 Coefficient: " + mode2_c.toFixed(2).toString()
      },
      mode3_label: {
          color: "var(--w0)",
          value: "Mode 2 Coefficient: " + mode3_c.toFixed(2).toString()
      }
  };
});

<​/d3>
```

# GLSL

I've used [twgl.js](https://twgljs.org) to allow me to play with fragment 
shaders.

<twgl id="mandelbrot">
 
 precision mediump float;

 // uniforms automatically handled behind the scenes
 uniform vec2 resolution;
 uniform float min_dim;
 uniform bool mouseover;
 uniform bool mousedown;
 uniform vec2 mouse;
 uniform vec2 mouse_click;
 uniform float click_elapsed;

 vec2 z0 = vec2(mouse.x - 0.5, mouse.y);
 
 vec3 colormap(float v) {
     // map interval [0, 1] to color
     //
     // use YCoCg color space for simplicity
     // https://en.wikipedia.org/wiki/YCoCg 
     
     float Y = pow(1. - pow(v - 1., 2.), 2.); // logistic on v [0, 1] -> [0, 1]
     float cr = (1. - cos(6.283 * v)) / 2.;   // radius in "hue space"
     float Cg = cr * sin(4. * Y + 3.);        // in [-1, 1]
     float Co = cr * cos(4. * Y + 3.);        // in [-1, 1]
     float R = Y + Co - Cg;
     float G = Y + Cg;
     float B = Y - Co - Cg;

     return vec3(R, G, B);
 }

 // iteration count
 const int iter = 100;
 const float fiter = 100.;
 float iterate(vec2 z, vec2 c) {

     vec2 w;
     float r2;
     float v;

     // iterate map
     for(int i=0; i < iter; i++) {

         // complex multiplication (^2)
         w.x = (z.x * z.x - z.y * z.y) + c.x;
         w.y = (2. * z.y * z.x)        + c.y;

         v = float(i);
         r2 = (w.x * w.x + w.y * w.y);

         if(r2 > 5.0) {
             break;
         }
         z.x = w.x;
         z.y = w.y;
     }

     // "real" iteration number using potential function
     if (v == (fiter - 1.)) {
         v = v / fiter;
     } else {
         v = (v - log2(log(r2)) * 0.5) / fiter;
     }

     return v;

 }

 void main() {

     vec2 c = vec2(((2. * gl_FragCoord.x) - resolution.x) / min_dim - 0.5,
                   ((2. * gl_FragCoord.y) - resolution.y) / min_dim);

     float v = iterate(z0, c);

     float rc2 = (z0.x - c.x) * (z0.x - c.x) + (z0.y - c.y) * (z0.y - c.y);
 
     vec4 value = vec4(colormap(v), 1.0);

     // display control point
     if (rc2 < 0.0001) {
         value = vec4(0.5, 0.5, 0.5, 1.0);
     }

     gl_FragColor = value;
}
 
</twgl>

<script>
onReady(function() {

 var man = shaders['mandelbrot'];
 
 man.uniforms.mouse = [0.5, 0];
    
 var first_run = false;
 function render(frame_number, time) {
    
     // render a first time
     if (!first_run) {
         first_run = true;
         man.render(man.uniforms);
     } 
     // render only when mouse is over
     else if (man.uniforms.mouseover) {
         man.render(man.uniforms);
     }
 }

 // only render when in view
 bindScrollTriggers(
     man.gl.canvas,
     function(){ 
         addAnimation(render);
     },
     function(){
         removeAnimation(render);
     }
 );
  
});
</script>

```GLSL
<twgl id="mandelbrot">
 
 precision mediump float;

 // uniforms automatically handled behind the scenes
 uniform vec2 resolution;
 uniform float min_dim;
 uniform bool mouseover;
 uniform bool mousedown;
 uniform vec2 mouse;
 uniform vec2 mouse_click;
 uniform float click_elapsed;

 vec2 z0 = vec2(mouse.x - 0.5, mouse.y);
 
 vec3 colormap(float v) {
     // map interval [0, 1] to color
     //
     // use YCoCg color space for simplicity
     // https://en.wikipedia.org/wiki/YCoCg 
     
     float Y = pow(1. - pow(v - 1., 2.), 2.); // logistic on v [0, 1] -> [0, 1]
     float cr = (1. - cos(6.283 * v)) / 2.;   // radius in "hue space"
     float Cg = cr * sin(4. * Y + 3.);        // in [-1, 1]
     float Co = cr * cos(4. * Y + 3.);        // in [-1, 1]
     float R = Y + Co - Cg;
     float G = Y + Cg;
     float B = Y - Co - Cg;

     return vec3(R, G, B);
 }

 // iteration count
 const int iter = 100;
 const float fiter = 100.;
 float iterate(vec2 z, vec2 c) {

     vec2 w;
     float r2;
     float v;

     // iterate map
     for(int i=0; i < iter; i++) {

         // complex multiplication (^2)
         w.x = (z.x * z.x - z.y * z.y) + c.x;
         w.y = (2. * z.y * z.x)        + c.y;

         v = float(i);
         r2 = (w.x * w.x + w.y * w.y);

         if(r2 > 5.0) {
             break;
         }
         z.x = w.x;
         z.y = w.y;
     }

     // "real" iteration number using potential function
     if (v == (fiter - 1.)) {
         v = v / fiter;
     } else {
         v = (v - log2(log(r2)) * 0.5) / fiter;
     }

     return v;

 }

 void main() {

     vec2 c = vec2(((2. * gl_FragCoord.x) - resolution.x) / min_dim - 0.5,
                   ((2. * gl_FragCoord.y) - resolution.y) / min_dim);

     float v = iterate(z0, c);

     float rc2 = (z0.x - c.x) * (z0.x - c.x) + (z0.y - c.y) * (z0.y - c.y);
 
     vec4 value = vec4(colormap(v), 1.0);

     // display control point
     if (rc2 < 0.0001) {
         value = vec4(0.5, 0.5, 0.5, 1.0);
     }

     gl_FragColor = value;
}
 
</twgl>
```
```javascript
<script>
onReady(function() {

 var man = shaders['mandelbrot'];
 
 man.uniforms.mouse = [0.5, 0];
    
 var first_run = false;
 function render(frame_number, time) {
    
     // render a first time
     if (!first_run) {
         first_run = true;
         man.render(man.uniforms);
     } 
     // render only when mouse is over
     else if (man.uniforms.mouseover) {
         man.render(man.uniforms);
     }
 }

 // only render when in view
 bindScrollTriggers(
     man.gl.canvas,
     function(){ 
         addAnimation(render);
     },
     function(){
         removeAnimation(render);
     }
 );
  
});
</script>
```
