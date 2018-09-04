# Static-Website

Static website generation from markdown.

**Repo Contents:**

```
.
├── content         Your content goes here
├── public          Generated files are put here
├── plugins         Python files for processing and manipulating content
├── theme           HTML templates, Javascript, and CSS
├── run.sh          Shell script to generate files and serve locally
├── pelicanconf.py  Contains basic settings for pelican
├── readme.md       You're reading it now
└── .gitignore      List of files ignored by git
```

# Setup

## Requirements

* [git](https://www.atlassian.com/git/tutorials/install-git)

* python3
    * [pelican](http://docs.getpelican.com/en/3.6.3/install.html)
    * [pygments](http://pygments.org/)
    * [python-bond](https://www.thregr.org/~wavexx/software/python-bond/)
    * [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

* [npm/node.js](https://www.npmjs.com/get-npm)
    * [katex](https://github.com/Khan/KaTeX)
    * [d3](https://d3js.org)
    * [jsdom](https://github.com/jsdom/jsdom)
    * [lightserver](https://www.npmjs.com/package/light-server)

## Installation

For me (using Linux and assuming `pip3` and `npm` commands are available):

* Install requirements

        pip3 install --user pelican markdown beautifulsoup4 python-bond pygments
        sudo npm install -g katex d3 jsdom lightserver

* Fork and clone the repo

    * [Fork](https://github.com/login?return_to=%2Fraabrp%2Frraabblog) this repo.

    * Clone the repo locally
    
            git clone <URL-of-forked-repo>

* Make `run.sh` executable

        chmod +x <path-to-local-copy-of-repository>/run.sh

# Usage

* run `run.sh` in the repo root
* edit the `content` directory and see auto-refreshed results in the browser
* [save changes](https://www.atlassian.com/git/tutorials/saving-changes) with
   git.
    * e.g. `git commit -a -m "Updated paragraph about my hopes and dreams"`
* push to (your fork of) this git repository
    * e.g. `git push`

**Note**: if you delete a source file which has already resulted in files being 
generated in `pubic`, the generated files will not be automatically removed. A
quick fix is to simply delete the generated files, or delete the public folder
and regenerate it anew with `run.sh`.
