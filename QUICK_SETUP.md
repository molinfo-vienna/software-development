This setup guide is for everyone wanting to setup their project quickly and easily for a molecular informatics project in python.

1. Get a proper IDE

    We recommend donwloading and installing <mark>VS Code</mark> for your project.
    There are numerous other IDEs (e.g. PyChamr, Spyer,...) but VS Code is lightweight and can be extended easily to the favour of your choice.

    To donwload and install our recommendation go to [VS Code Homepage](https://code.visualstudio.com/download). Follow the instructions for your operating system.

2. Setup your python package manager

    The standard python package manager is [pip](https://pypi.org/project/pip/). It is built-in to python and can install a huge variety of packages from different sources. It installs packages into a projects's global python environment and is accessed by all projects.
    As soon as you need to manage different versions of particular packages that might interfer with other package dependencies, conflicts may arise.

    For this and other reasons we recommend using [conda](https://code.visualstudio.com/download) as the main python package manager. It allows to create virtual environments with different versions of packages.
    If packages are not available, use pip to install them into the global environment.
    We encourage the use of different environments for different projects. 
    Therefore make it easy for collaborators to set up the same environment without caring too much about dependencies.





