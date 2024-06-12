# Integrated Development Environment Software (IDE)

### General

We recommend downloading and installing `VS Code` for your project.
There are numerous other IDEs (e.g. PyCharm, Spyder,...) but VS Code is lightweight and can be extended easily to the favor of your choice.

To download and install our recommendation go to [VS Code Homepage](https://code.visualstudio.com/download). Follow the instructions for your operating system.


### Setup your python package manager

The standard python package manager is [pip](https://pypi.org/project/pip/). It is built-in to python and can install a huge variety of packages from different sources. It installs packages into a project's global python environment and is accessed by all projects.
As soon as you need to manage different versions of particular packages that might interfere with other package dependencies, conflicts may arise.

For this and other reasons we recommend using [conda](https://docs.conda.io/projects/conda/en/latest/) as the main python package manager (or distribution). It allows to create virtual environments with different versions of packages.
If packages are not available, use pip to install them into the global environment.
We encourage the use of different environments for different projects. 
Therefore make it easy for collaborators to set up the same environment without caring too much about dependencies.

Conda can be downloaded for your operating system [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Follow the instructions given and save it at a convenient location ("/path/to/miniconda/").

After the installation process is finished, create a new environment with a fitting and easy-to-remember name as you need to activate it frequently.

Regarding conda - a fun read about myths and misconceptions of conda can be found [here](https://jakevdp.github.io/blog/2016/08/25/conda-myths-and-misconceptions/)

**Local installation**
When working with your own code as a package and you want to reference it locally, it is often recommended to do a "local" python install via ```pip install -e .``` - this works only if you are in the root folder of your package. This command will insert your new project into your Python site-packages folder so that it can be found in any directory on your computer.

__Next Chapter:__ [__Project Structure__](/PROJECT_STRUCTURE.md)