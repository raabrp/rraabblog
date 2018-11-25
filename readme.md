# Static-Website

Static website generation from markdown.

**Repo Contents:**

```
.
├── /content        Your content goes here (ignored by git)
├── /drafts         Drafts of content (not turned into HTML; ignored by git) 
├── /public         Generated HTML files are put here (ignored by this repo)
├── /plugins        Python files for processing and manipulating content
├── /theme          HTML templates, Javascript, and CSS
├── .gitignore      List of files ignored by git
├── licence.txt     MIT licence
├── pelicanconf.py  Contains basic settings for pelican
├── readme.md       You're reading it now
├── run.sh          Shell script to generate files and serve locally
└── todo.md         Plans for the project
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
        sudo npm install -g katex d3 jsdom light-server

    Personal note: I had to make sure to include
        `~/.local/bin` in my PATH and set
        `/usr/lib/node_modules/` as my NODE_PATH

* Fork and clone the repo

    * [Fork](https://github.com/login?return_to=%2Fraabrp%2Frraabblog) this repo.

    * Clone the repo locally
    
            git clone <URL-of-forked-repo>

* Make `run.sh` executable

        chmod +x <path-to-local-copy-of-repository>/run.sh
        
## Configuration

Initialize `/public` as a git repository to be hosted online (e.g. with [github 
pages](https://pages.github.com))

### Custom Domains

See https://reillyraab.com/about.html for how I've set things up for myself in
terms of hosting with my own domain name. A technical step not mentioned there 
is the inclusion of a file called `CNAME` in the `/public` directory/repository
which states the name of my domain. Reference
https://github.com/raabrp/raabrp.github.io for the contents of my own `/public`
directory/repository.

# Usage

* run `./run.sh` in the repo root
* edit the `content` directory and see auto-refreshed results in the browser
* navigate to `/public`, commit your changes, and push.
    * e.g. `git commit -a -m "Added limited bio to About page"`
    * e.g. `git push`
    
For those still learning to use git (we were all here once), Atlassian has a 
decent [tutorial](https://www.atlassian.com/git/tutorials/saving-changes).

Finally, dig through `pelicanconf.py`, `/theme`, and `/plugins` and feel free to
make them your own. I've attempted to document them appropriately.

**Note**: if you delete a source file (e.g. in `/contents`) which has already
resulted in files being generated in `/pubic`, the generated files will NOT be
automatically removed.
