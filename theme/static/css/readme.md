# We separate CSS by role

* main        - layout
* page        - if pages should differ from articles
* decorations - borders, font, etc
* interactive - dynamic content. menu, hover, tooltips, etc.
* color-x-y   - colors

# Color

## Overview

* all css dealing with colors is separated from css affecting layout
* techical aspects of color are discussed lightly in generate.py
* python uses jinja2 to generate a few scss files with transformed colors.

## Requirements

pip3
- jinja2
- scikit-image

## Usage

update colors in generate.py / modify the template, then:

```
$ python3 colors.py
```
