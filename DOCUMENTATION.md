# Documentation

If you want people to use your project and code, write proper documentation!
Start as soon as possible! 
Its more fun to produce code right away, but crucial to produce proper documentation as soon as possible. 
We would recommend filling up your README.md with what your project `can do`, `how to install` it, including `requirement files`, `how to use` it, `what licence` you have and `where to ask questions`.

Also define proper documentation for classes, methods, and scripts.
Without knowing what goes in, what it does, and what comes out how of any code, its hard for people to trust your code.
Moreover, after some time it is often hard for yourself to remember what you did over the years working on one or several projects.

In general we recommend the following sites for further details:
* [Real Python](https://realpython.com/documenting-python-code/) offers an in depth guide for documenting python code.
* [The Hitchhiker's Guide to Python](https://docs.python-guide.org/writing/documentation/) is not as overloaded and gives a brief insight into another tool ([Sphinx](https://www.sphinx-doc.org/en/master/)).

Many `README.md` files include a series of badges at the top.
These badges are not only visual indicators of certain information---whether the repo is in a healthy state with passing tests, which channels are available for obtain the tool, which version number is current, and how many times the software has been downloaded---they provide quick links to a variety of useful integrated services.

There are many tools that can be used to write documentation. The easiest to start with is the GitHub wiki, which uses markdown syntax just like the rest of GitHub.

### GitHub wiki

If you're already hosting your project on [GitHub](http://github.com), perhaps the easiest to start with is [Github wiki](https://help.github.com/articles/about-github-wikis/) which uses the same [GitHub markdown syntax](https://guides.github.com/features/mastering-markdown/).
GitHub wikis are [version controlled](https://help.github.com/articles/viewing-a-wiki-s-history-of-changes/), and can even be [edited like a standard Git repository](https://help.github.com/articles/adding-and-editing-wiki-pages-locally/).

Helpful guide on GitHub wikis:
https://guides.github.com/features/wikis/

Some good examples of wiki-based documentation:
* [`D3.js`](https://github.com/d3/d3/wiki): https://github.com/d3/d3/wiki

### Sphinx

If you need something slightly more powerful, consider using [Sphinx](http://www.sphinx-doc.org/en/1.4.8/), which has excellent support for producing beautiful Python documentation.
From the same documentation source, you can build both HTML (online) and PDF (offline) versions, among [many others supported](http://www.sphinx-doc.org/en/1.4.8/builders.html).

Hosting a [sphinx](http://www.sphinx-doc.org/en/1.4.8/) project can be tricky on its own, but is almost trivial if you have a public GitHub repository, since you can use [Read the Docs](https://docs.readthedocs.io/en/latest/getting_started.html) (RTD), which automatically rebuilds and hosts the documentation every time you commit to your repository.
This [template](https://github.com/readthedocs/template) and this [tutorial](http://www.sphinx-doc.org/en/stable/tutorial.html) can help you easily get started.

If you're using [`conda`](http://conda.pydata.org/docs/) for your code, you may want to check out [this step by step guide](https://github.com/choderalab/Protons/blob/master/howto-documentation.rst) on setting up a `conda` project with [RTD](https://readthedocs.org).

Some good examples of Sphinx documentation:

* Sphinx docs, hosted on Read the Docs: [protons](http://protons.readthedocs.io) | [ensembler](http://ensembler.readthedocs.io)
* Sphinx docs, built by travis and hosted on S3: [openmm](http://docs.openmm.org/7.1.0/userguide/index.html) | [mdtraj](http://mdtraj.org/) | [pymbar](http://pymbar.org/) | [yank](http://getyank.org) | [pymc](https://github.com/pymc-devs/pymc/tree/master/docs)

### Other documentation schemes

* [readme.io](http://readme.io): A collaborative system for writing documentation
* [GitBook](https://www.gitbook.com): An online collaborative publishing toolchain

Some useful badges:
- [AppVeyor badge](https://www.appveyor.com/docs/status-badges/)
- [pypi version and downloads badges](http://codeinthehole.com/writing/pypi-readme-badges/)
- [Anaconda Cloud version and download badge](https://anaconda.org/anaconda/anaconda/badges)
- [Depsy badge](http://blog.impactstory.org/introducing-depsy/)
- [Zenodo DOI badge](https://guides.github.com/activities/citable-code/)

__Next Chapter:__ [__Packaging and Continuous Deployment__](/PACKAGING.md)