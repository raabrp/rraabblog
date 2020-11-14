# Static Website Generation

Static website generation from markdown using Pelican with a few custom 
extensions. Currently configured to generate a website in a subdirectory called
`public`, which is its own git repo. Specifically, it's a repo which is set up
as my "github pages" (https://github.com/raabrp/raabrp.github.io), available 
online at https://raabrp.github.io or https://reillyraab.com

**Repo Contents:**

```
.
├── /content          Your content goes here (ignored by git)
| ├ /articles
| └ /pages
| ...additional static content...
|
├── /content_example  Minimal example content for reference
| ├ /articles
| └ /pages
|
├── /drafts           Drafts of content (not turned into HTML; ignored by git) 
├── /public           Generated HTML files are put here (ignored by this repo)
├── /plugins          Python files for processing and manipulating content
├── /theme
| ├ /templates        HTML templates (Jinja)
| └ /static           Static resources (Javascript, CSS)
|
├── .gitignore        List of files ignored by git
├── licence.txt       MIT licence
├── pelicanconf.py    Contains basic settings for pelican
├── readme.md         You're reading it now
├── run.sh            Shell script to generate files and serve locally
└── todo.md           Plans for the project
```

# Setup

## Requirements

* [git](https://www.atlassian.com/git/tutorials/install-git)

* python3
    * [pelican](http://docs.getpelican.com/en/3.6.3/install.html)
    * [pygments](http://pygments.org/)
    * [python-bond](https://www.thregr.org/~wavexx/software/python-bond/)
    * [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    * [pbkdf2](https://www.dlitz.net/software/python-pbkdf2/)
    * [pycrypto](https://pypi.org/project/pycrypto/)

pbkdf2 and pycrypto are used only when generating password-protected content.
(The password for the encryption demo in `content_example` is `encrypted`)

* [npm/node.js](https://www.npmjs.com/get-npm)
    * [katex](https://github.com/Khan/KaTeX)
    * [lightserver](https://www.npmjs.com/package/light-server)

See [this](https://medium.com/@ExplosionPills/dont-use-sudo-with-npm-still-66e609f5f92)
post on why `sudo npm` is worth avoiding (and how to not need it).

## Installation

* Fork and clone the repo

    * [Fork](https://github.com/login?return_to=%2Fraabrp%2Frraabblog) this repo.

    * Clone the repo locally
    
            git clone <URL-of-forked-repo>
            cd rraabblog

* Install requirements

With pip:

        pip3 install --user pelican markdown beautifulsoup4 python-bond pygments
        pip3 install --user pbkdf2 pycrypto
        
Alternativel, with conda:

        conda update -n base -c defaults conda
        conda env create -f environment.yml
        direnv allow .

Then install node.js packages

        npm install -g katex light-server

Personal note: I had to make sure to include `~/.local/bin` in my PATH and set `/usr/lib/node_modules/` as my NODE_PATH

* Make `run.sh` executable

        chmod +x <path-to-local-copy-of-repository>/run.sh
        
## Configuration

Initialize `/public` as a git repository to be hosted online (e.g. with [github 
pages](https://pages.github.com))

### Custom Domains

I use:
* [github pages](https://pages.github.com) for hosting, as mentioned.
* [namecheap](https://www.namecheap.com) for domain registration / nameservers.
* [cloudflare](https://www.cloudflare.com) for dns, caching, and SSL.

My `public` directory has a file called 
[`CNAME`](https://en.wikipedia.org/wiki/CNAME_record) containing only
`reillyraab.com`.

# Usage

* run `./run.sh` in the repo root
* edit the `content` directory and see auto-refreshed results in the browser
* navigate to `/public`, commit your changes, and push.
    * e.g. `git commit -a -m "Notes about commit"`
    * e.g. `git push`
    
For those learning to use git (we were all here once), Atlassian has a decent
[tutorial](https://www.atlassian.com/git/tutorials/saving-changes).

Finally, dig through `pelicanconf.py`, `/theme`, and `/plugins` and feel free to
make them your own. I've attempted to document them appropriately.

**Note**: if you delete a source file (e.g. in `/contents`) which has already
resulted in files being generated in `/pubic`, the generated files will NOT be
automatically removed.
