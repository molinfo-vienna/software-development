# Documentation and Linting

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

Some useful badges:
- [AppVeyor badge](https://www.appveyor.com/docs/status-badges/)
- [pypi version and downloads badges](http://codeinthehole.com/writing/pypi-readme-badges/)
- [Anaconda Cloud version and download badge](https://anaconda.org/anaconda/anaconda/badges)
- [Depsy badge](http://blog.impactstory.org/introducing-depsy/)
- [Zenodo DOI badge](https://guides.github.com/activities/citable-code/)


- **Use Docstring Documentation**: Adhere to PEP 257 guidelines for docstring conventions, ensuring clear and consistent documentation throughout the codebase.
- **Automate Documentation Checks**: Integrate tools like Docsig, Interrogate, and Pydocstyle to automate documentation validation and enforce consistency.
  - **Docsig**: Checks that the docstring of a function matches its signature, ensuring consistency and accuracy. `docsig -C -D -m -N -o -p .`
  - **Interrogate**: Automates the validation of documentation against the code it documents, ensuring accuracy and completeness. `interrogate -O -vv .`
  - **Pydocstyle**: Enforces adherence to docstring conventions, enhancing code readability and maintainability. `pydocstyle .`
- **Parameter Definition and Documentation**: Every function parameter should be clearly defined with appropriate types and descriptive comments, enhancing maintainability and ease of use. The above tools can help enforce these practices. To install these tools, use `pip install docsig interrogate pydocstyle`.

There are many tools that can be used to write documentation. The easiest to start with is the GitHub wiki, which uses markdown syntax just like the rest of GitHub.

### Linting

Linting is the process of running a program that will analyze code for potential errors and inconsistencies. Linters are tools that help ensure that your code is free from syntax errors, structural problems, and other common sources of errors that could lead to bugs in the execution of the program. They also enforce a consistent coding style, making sure that the code adheres to the guidelines and standards that a development team has set. This helps in maintaining the code readability and can significantly speed up the maintenance process as well as onboarding new developers.


### Type Hinting

Type hinting is a practice introduced in Python 3.5 that involves specifying the expected data types of function arguments and return values. While Python is a dynamically typed language, adding type hints helps with static analysis of the code, improving its readability and reducing runtime errors. It allows developers and tools to infer how functions and classes are supposed to be used and can greatly aid in catching type-related mistakes early in the development cycle.


### Code Style 

Code style refers to a set of guidelines or standards governing the writing of code. These standards can include rules about how to name variables, how to structure classes, the length of lines of code, and more. Adhering to a consistent code style improves the readability and maintainability of code, making it easier for other developers to read, understand, and collaborate on. It also promotes a unified look and feel of the codebase, which is crucial in reducing cognitive load when switching between different parts of the project.

With these practices in place, developers can avoid common pitfalls in their code, making their software more robust and easier to manage. In the following section, we'll explore some essential tools that help enforce these good practices, enhancing your coding workflow and ensuring that your Python projects are of the highest quality.

### Tools to achieve the above

- **Implement Linting Tools**: Utilize linting tools such as Flake8, Black, Bandit, Isort and Mypy to enforce coding standards and promote consistent code style across the project.
  - **Bandit**: Identifies potential security issues in Python code. `bandit -r --skip=B404,B603,B602 .`
  - **Black**: Formats code for consistent style, reducing the need for stylistic reviews. `black --check .`
  - **Flake8**: Analyzes code to catch syntax errors, bugs, and stylistic errors. `flake8 --extend-ignore=D203,E203,E501,W503 .`
  - **Isort**: Sorts imports alphabetically and automatically separates them into sections. `isort --profile black --check-only .`
  - **Mypy**: Checks and enforces type hints, improving code reliability and aiding in early detection of type-related errors. First install missing types: `mypy --install-types --non-interactive`. Then run mypy: `mypy --ignore-missing-imports --disallow-any-generics --disallow-untyped-defs --no-implicit-optional --disallow-incomplete-defs .`
  - **PyLint**: Another popular tool for enforcing coding standards and identifying potential issues. First install all required packages: `pip install $(find /app/linting/ -name "requirement*" -type f -printf ' -r %p')`. Then run PyLint on all files: `find . -type f -name "*.py" | xargs pylint -d C0301,R0913,W1202 --ignored-modules "rdkit"`
- **Implementation**: These tools should be configured to run in a GitHub Actions workflow using local runners to ensure that every commit adheres to established coding standards. To install these tools, use `pip install flake8 black bandit isort mypy pylint`.

Look at an automated example [here](/GITHUB_ACTIONS.md##GitHub-Actions-Workflow-Example) that includes linting tools and a GitHub Actions workflow.


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

__Next Chapter:__ [__Packaging and Continuous Deployment__](/PACKAGING.md)