---
slug: test
d3: true
title: Markdown Demo
date: 2018-01-01
last_updated: 2018-07-20
---

[TOC]


# Article Meta

The top of this file includes

```
---
slug: test
status: draft
d3: true
title: Markdown Demo
date: 2018-01-01
last_updated: 2018-07-20
---

[TOC]

```

* `slug`: location of generated html file
* `title`: Appears at top of page
* `date`: Date shown and sorted by on main page
*  last_updated: Date last updated
* `status: draft` no link generated in index
*  d3: optional use of d3 library
push it with git (content is put in ignored `drafts` folder).
* `[TOC]`: Includes table of contents (optional**

# Text

Officia officiis est in illum ipsam id. Soluta ipsam fugit reprehenderit 
praesentium earum ut ut. Aut eaque rerum illo sint est sequi. Facere numquam ad 
fuga quod impedit. Impedit reiciendis iure odit aperiam et quo doloribus et.

Mollitia quo molestiae beatae veritatis et quae. Repellat corporis labore velit.
Laborum nostrum ut non qui doloremque tempora. Et assumenda architecto illum 
minus labore quia. Optio illum rerum autem.

Maxime quo quod excepturi. Est adipisci magnam nulla iste neque et cumque 
itaque. Cum vitae natus est aut aliquam. Ut blanditiis deleniti consequatur 
placeat modi consequatur sed. Minus magnam repellendus molestiae. Sint hic illo
voluptatem veniam maiores dolore.


```
Officia officiis est in illum ipsam id. Soluta ipsam fugit reprehenderit 
praesentium earum ut ut. Aut eaque rerum illo sint est sequi. Facere numquam ad 
fuga quod impedit. Impedit reiciendis iure odit aperiam et quo doloribus et.

Mollitia quo molestiae beatae veritatis et quae. Repellat corporis labore velit.
Laborum nostrum ut non qui doloremque tempora. Et assumenda architecto illum 
minus labore quia. Optio illum rerum autem.

Maxime quo quod excepturi. Est adipisci magnam nulla iste neque et cumque 
itaque. Cum vitae natus est aut aliquam. Ut blanditiis deleniti consequatur 
placeat modi consequatur sed. Minus magnam repellendus molestiae. Sint hic illo
voluptatem veniam maiores dolore.
```

# Headers

## Sub Header

### Subheader

#### Subheader


```md
# Headers

## Sub Header

### Subheader

#### Subheader
```

# Horizontal Rule

***


```md
***
```

# Text Decoration

**Similique** *asperiores* nihil `ad aut` ***aliquam totam***. 


```md
**Similique** *asperiores* nihil `ad aut` ***aliquam totam***.
```

# Links

Tenetur rem [deleniti](http://www.example.com) magan
[*consequatur*](http://www.example.com) at non.


~~~md
Tenetur rem [deleniti](http://www.example.com) 
[*dconsequatur*](http://www.example.com) at non.
~~~

# Block Quotes

> Beatae officiis quae aut iusto rerum. Non amet molestiae et. 
> Itaque molestiae temporibus et temporibus nobis nobis. 
> Sequi ut aut libero maiores.
>
> Dolores illum in iure quae. 
> Magnam tempore non illo odit provident fuga. 
> Id odit in aut doloremque rerum ut aliquam voluptatem. 
> Velit molestiae minima architecto quam. Id eum id illum. 
> Reiciendis qui et eos commodi corrupti.


```md
> Beatae officiis quae aut iusto rerum. Non amet molestiae et. 
> Itaque molestiae temporibus et temporibus nobis nobis. 
> Sequi ut aut libero maiores.
>
> Dolores illum in iure quae. 
> Magnam tempore non illo odit provident fuga. 
> Id odit in aut doloremque rerum ut aliquam voluptatem. 
> Velit molestiae minima architecto quam. Id eum id illum. 
> Reiciendis qui et eos commodi corrupti.
```

# Footnotes

Footnote.[^unique string]

[^unique string]: Footnote written separately


```md
Footnote.[^unique string]

[^unique string]: Footnote written separately
```

# Syntax Highlighting

```python
@requires_authorization
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print 'Gre\'ater'
    return (param2 - param1 + 1 + 0b10l) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''
```


```md
~~~python
@requires_authorization
def somefunc(param1='', param2=0):
    r'''A docstring'''
    if param1 > param2: # interesting
        print 'Gre\'ater'
    return (param2 - param1 + 1 + 0b10l) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''
~~~
```

**-- or --**

* swapping `~~~` and <code>```</code>
* writing `:::python` indented, followed by indented code block
* writing `!#python` indented, followed by indented code block (for line numbers)
* any pygments-recognized language may be used

# Images

![Happy Cookie Monster](https://slides.yihui.name/gif/happy-elmo.gif)


```
![Happy Cookie Monster](https://slides.yihui.name/gif/happy-elmo.gif)
```

# Bullet Points

* Item 1
    * sub-item a
* Item 2
    * sub-item b
        * sub-sub-item i
* Item 3


```md
* Item 1
    * sub-item a
* Item 2
    * sub-item b
        * sub-sub-item i
* Item 3
```

# Lists

1. This one
2. That one
3. The other thing


```md
1. This one
2. That one
3. The other thing
```

# Tables

| Sepal.Length| Sepal.Width| Petal.Length| Petal.Width|Species |
|-------------|------------|-------------|------------|--------|
| 5.1         | 3.5        | 1.4         | 0.2        |setosa  |
| 4.9         | 3.0        | 1.4         | 0.2        |setosa  |
| 4.7         | 3.2        | 1.3         | 0.2        |setosa  |
| 4.6         | 3.1        | 1.5         | 0.2        |setosa  |
| 5.0         | 3.6        | 1.4         | 0.2        |setosa  |
| 5.4         | 3.9        | 1.7         | 0.4        |setosa  |



```md
| Sepal.Length| Sepal.Width| Petal.Length| Petal.Width|Species |
|-------------|------------|-------------|------------|--------|
| 5.1         | 3.5        | 1.4         | 0.2        |setosa  |
| 4.9         | 3.0        | 1.4         | 0.2        |setosa  |
| 4.7         | 3.2        | 1.3         | 0.2        |setosa  |
| 4.6         | 3.1        | 1.5         | 0.2        |setosa  |
| 5.0         | 3.6        | 1.4         | 0.2        |setosa  |
| 5.4         | 3.9        | 1.7         | 0.4        |setosa  |
```

# Injected HTML \ Javascript

<div id="example">
<script type="text/javascript">
document.getElementById("example").innerHTML="Hello, world!";
</script>
</div>


~~~html
<div id="example">
<script type="text/javascript">
    document.getElementById("example").innerHTML="Hello, world!";
</script>
</div>
~~~

*Note: `<script>` element must be inside `<div>`*

# Math (KaTeX)

Inline math: $\alpha > \beta$.


```
Inline math: $\alpha > \beta$.
```

As a block:

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

# D3 Chart

***Note***:
List of settings at top of markdown file must include
`d3: true`

I'm still working out how to do charting most effectively. Mathbox is high
on the to-do list for this purpose.

But, we can currently do this (see below) right in our markdown source using
a custom extension, which gives us some nifty side-effects like only rendering
content in view, nicely reusing components (such as lines with adaptive 
resampling), and allowing parameterized animations, etc.:

<d3 height="50">

/*
 * Uses components Line and Text from `theme/static/js/chart_components.js`
 * See `theme/static/js/charts.js`
 * See `plugins/charts/charts.py`
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
  var mode2_c = Math.sin(Tau * p * 3 - .1) * 0.2;
  
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
          color: "#fff"
      },
      arclength_label: {
          color: "#fff",
          value: "Arclength: " + (arc_length / min_arc_length)
                                  .toFixed(2).toString()
      },
      mode1_label: {
          color: "#fff",
          value: "Mode 0 Coefficient: " + mode1_c.toFixed(2).toString()
      },
      mode2_label: {
          color: "#fff",
          value: "Mode 1 Coefficient: " + mode2_c.toFixed(2).toString()
      },
      mode3_label: {
          color: "#fff",
          value: "Mode 2 Coefficient: " + mode3_c.toFixed(2).toString()
      }
  };
});

</d3>



(where `D3` should be lowercase)

```javascript

<D3 height="50">

/*
 * Uses components Line and Text from `theme/static/js/chart_components.js`
 * See `theme/static/js/charts.js`
 * See `plugins/charts/charts.py`
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
          color: "#fff"
      },
      arclength_label: {
          color: "#fff",
          value: "Arclength: " + (arc_length / min_arc_length)
                                  .toFixed(2).toString()
      },
      mode1_label: {
          color: "#fff",
          value: "Mode 0 Coefficient: " + mode1_c.toFixed(2).toString()
      },
      mode2_label: {
          color: "#fff",
          value: "Mode 1 Coefficient: " + mode2_c.toFixed(2).toString()
      },
      mode3_label: {
          color: "#fff",
          value: "Mode 2 Coefficient: " + mode3_c.toFixed(2).toString()
      }
  };
});

</D3>
```
