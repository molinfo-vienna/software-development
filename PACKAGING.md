# Packaging

Anyone who has tried to compile and install [`scipy`](http://scipy.org/) from source can attest that manually installing complex Python dependencies can be a time-consuming nightmare.
If your code makes use of the many wonderful Python packages out there as dependencies, it can quickly become unmanageable to expect users to install these dependencies by hand.

*Don't* simply list all the "prerequisites" your code requires and expect the user to figure out how to install them.
Users that are new to the Python ecosystem may try to install them in any manner of ways, and it's not guaranteed that they will manage to install fully compatible versions.
It is almost guaranteed they will not enjoy installing a large list of dependencies manually.

The more we, as tool providers, can do to simplify the installation process, the better.
If prospective users can easily install your tool and get up and running quickly, they are much more likely to use your tool, get something done, and cite your work.

By following the recommendations in the previous chapters you are already at a good path.

## Packaging solutions

### The Python Package Index (PyPI)

**You dont necearrily need to publish your code to PyPI.** in order to have a "package". You can also install your package locally from your source folder via:
```bash
pip install .
```

If your package is pure Python, it's easy to package and deploy to a very wide audience via the [Python Package Index](https://pypi.python.org/pypi).
This site greatly simplifies installation from the user perspective via the tool [`pip`](https://pip.pypa.io) which is available almost universally in common Python distributions.
Installation of a tool like [`pymbar`](https://github.com/choderalab/pymbar) is simplified to:
```bash
pip install pymbar
```
This automatically installs the specified package and its dependencies---which must also be available through PyPI---into the user's current Python installation.
Note that if this is a *system* Python installation, `pip install <packagename>` may ask for an administrator or root password so that the package can be installed into the system Python installation.
This is highly discouraged: We recommend that, whenever possible, user-space Python installations, such as the [Miniconda minimal Python install](http://conda.pydata.org/miniconda.html) installed into the user's home directory, be used.
The user can also [manage multiple environments this way](http://conda.pydata.org/docs/using/envs.html), in case different incompatible dependency versions are needed for different toolchains.

Packages with compiled components or binary libraries that must be distributed alongside them can generally not be deployed via PyPI.
While this is changing with wider support for Python wheels (see [PEP 427](https://www.python.org/dev/peps/pep-0427/), [PEP 491](https://www.python.org/dev/peps/pep-0491/), and [PEP 513](https://www.python.org/dev/peps/pep-0513/)), the recommended approach for codes that depend on platform-specific libraries is the `conda` scheme described below.

### Preparing Your Package

**Structure Your Project**: Organize your project files in a directory with a clear structure. Typically, this includes:
   - A `<module_name>/` directory where your package code resides.
   - A `tests/` directory for your unit tests.
   - Necessary files like `README.md`, `LICENSE`, `pyproject.toml`, and `requirements.txt`.

Check out at the details about [gitignore](/GITIGNORE.md), [pyproject.toml](/PROJECT_TOML.md), [setup.cfg](/SETUP.md), [__init__.py](/INIT.md), and [requirement.txt](/REQU.md).
Also look into the [template](/template/README.md) for a project.

**Create a `requirements.txt` File**: This file should list all the Python packages that your code depends on.

**Create a `pyproject.toml` File**: This script is essential for packaging your project. It should include metadata about your package like its name, version, author, and more. Dependencies listed in `requirements.txt` should be included under `install_requires` to ensure they are installed when your package is installed.
```toml
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
dynamic = ["dependencies", "optional-dependencies"]
name = "<module_name>"
authors = [
    {name = "Contributor 1"},
    {name = "Contributor 2"}
]
description = "<description>"
version = "<version>"
readme = "README.md"

[tool.setuptools.dynamic]
dependencies = {file = "requirements.txt"}

[tool.setuptools.dynamic.optional-dependencies]
all = {file = ["requirements_1.txt", "requirements_2.txt"]}
one = {file = ["requirements_1.txt"]}
two = {file = ["requirements_2"]}

[tool.setuptools.packages.find]
exclude = ["tests", "docs"]

[tool.setuptools.package-data]
"<module_name>" = ["py.typed"]
```

#### Distributing your code with PyPI

If you have a pure Python package you would like to upload to PyPI and have already structured it to be installable by a `setup.py` that makes use of [`distutils`](https://docs.python.org/3/library/distutils.html), uploading your package is very easy.
This [tutorial](https://packaging.python.org/tutorials/packaging-projects/) provides a gentle introduction to the whole process, but once everything is structured correctly, uploading is as simple as:
```bash
python setup.py register -r pypi
python setup.py sdist upload -r pypi
```
It is *highly recommended* that you first upload your package to the [PyPI testing site](https://testpypi.python.org) before uploading it to the live PyPI.

**Versioning**: Maintain clear versioning that adheres to semantic versioning standards. This helps users understand the extent of changes in each release.

### Conda

The [Conda package manager](http://conda.pydata.org) was developed as a solution to the fact that installing anything with platform-specific or binary dependencies via PyPI was essentially impossible.
You can read about the problems that `conda` attempts to solve in [this excellent blog piece](https://www.continuum.io/blog/developer-blog/python-packages-and-environments-conda), and learn about its [advanced](https://www.continuum.io/blog/developer/advanced-features-conda-part-1) [features](https://www.continuum.io/blog/developer/advanced-features-conda-part-2).
Since its inception, it has grown into a robust, stable way to deploy scientific Python packages that often depend on complex compiled code for maximum performance via the [Anaconda cloud](https://anaconda.org).

While users with `pip` can in principle obtain `conda` via
```bash
pip install conda
```
the preferred way to create a new `conda`-enabled minimal Python distribution is via the minimal [`miniconda`](http://conda.pydata.org/miniconda.html) distribution from [continuum.io](https://www.continuum.io/downloads).

For example, on a Linux cluster, you can install a fully functional `conda`-enabled Python distribution with
```bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh # fetch miniconda installer
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3 # install it automatically
export PATH="$HOME/miniconda3/bin:$PATH" # add it to your PATH
```
See the [`conda` quick install instructions](http://conda.pydata.org/docs/install/quick.html) for more on getting started quickly.

Once `conda` is installed, installation of tools with complex dependencies can then be done via [`conda install`](http://conda.pydata.org/docs/using/pkgs.html#install-a-package):
```bash
# Install seaborn, jupyter, and scipy
conda install --yes seaborn jupyter scipy
```

There are several ways to make use of [`conda`](http://conda.pydata.org) and the [Anaconda cloud](https://anaconda.org) to distribute your software:

#### Conda-forge

[Conda-Forge](https://conda-forge.github.io/) has emerged as the community standard way to automate release builds and uploads to the Anaconda cloud for community-developed codes.
Excellent documentation is available for [adding a recipe](https://conda-forge.github.io/#add_recipe) for automatically building your software for Windows, Linux, and OSX, provided it can easily be built using only `conda`-installable dependencies.

#### Creating your own build process (e.g. Omnia)

The [Omnia](http://www.omnia.md/) software consortium was formed to make deployment of high-performance computational chemistry codes that can take advantage of GPU computing (such as [OpenMM](http://openmm.org)) easy, and to nucleate a community of interoperable codes for computational chemistry.
The [Omnia build system](https://github.com/omnia-md/conda-recipes/blob/master/README.md) is similar to [Conda-Forge](https://conda-forge.github.io/), but uses specialized build infrastructure that provides CUDA and OpenCL capabilities.
Instructions for contributing a recipe for building and deploying your code through Omnia can be found [here](https://github.com/omnia-md/conda-recipes/blob/master/README.md#contributing-a-recipe).

## Template

Please also check out a working template [here](https://github.com/basf/cheminformatics_ci_cd_template)

__Next Chapter:__ [__Advanced_CI_CD__](/ADVANCED_CI_CD.md)
__Back:__ [__README__](/README.md)