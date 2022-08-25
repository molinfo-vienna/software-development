This setup guide is for everyone wanting to setup their project quickly and easily for a molecular informatics project in python.
In order to maximice collaborations and reasuability of each project, we recommend to make a package out of your project.
This allows for easy access of your code, reduce the time to implement new features, and collaborate. 
If you are working on sensitive topics that should not be public, you do not have to deploy to [Conda](https://anaconda.org/) or [PyPI](https://pypi.org/).

1. Get a proper IDE

    We recommend donwloading and installing <mark>VS Code</mark> for your project.
    There are numerous other IDEs (e.g. PyChamr, Spyer,...) but VS Code is lightweight and can be extended easily to the favour of your choice.

    To donwload and install our recommendation go to [VS Code Homepage](https://code.visualstudio.com/download). Follow the instructions for your operating system.


2. Setup your python package manager

    The standard python package manager is [pip](https://pypi.org/project/pip/). It is built-in to python and can install a huge variety of packages from different sources. It installs packages into a projects's global python environment and is accessed by all projects.
    As soon as you need to manage different versions of particular packages that might interfer with other package dependencies, conflicts may arise.

    For this and other reasons we recommend using [conda](https://docs.conda.io/projects/conda/en/latest/) as the main python package manager. It allows to create virtual environments with different versions of packages.
    If packages are not available, use pip to install them into the global environment.
    We encourage the use of different environments for different projects. 
    Therefore make it easy for collaborators to set up the same environment without caring too much about dependencies.

    Conda can be downloaded for your operating system [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Follow the instructions given and safe it at a convenient location ("/path/to/miniconda/").

    After the installation process is finished, create a new environment with a fitting and easy to remember name as you need to activate it frequently.

    **Local installation**
    When working with your own code as a package and you want to reference it locally, it is often recommended to do a "local" python install via pip install -e .. This command will insert your new project into your Python site-packages folder so that it can be found in any directory on your computer.
    
3. Structure your project

    Giving structure to your project is of uttermost importance - no matter what you are doing.

    There are many ways of how to structure your python software project - be it on your own or via a tamplate.

    In general, a good practice is to separate the various elements of your software project into separate locations. A software project is not just the code needed to perform its tasks, but also to document and deploy.

    **Give your own basic structure**

    A possible outline of your project could look like the following:
    ```
    project/
        devtools/
            README.md
            conda-recipe/
                meta.yaml
                build.sh
                bld.bat
                README.md
        docs/
        examplepackage/
        tests/
            data/
            reference_data.csv
            __init__.py
            test_examplepackage.py
        __init__.py
        examplepackage.py
        LICENSE.md
        README.md
        setup.py
        .travis.yml
        .appveyor.yml
        .gitignore
    ```

    ***root directory***

    The root directory should contain the primary `setup.py` file for the project. When 
    

    **Cookiecutter**

    We recommoned to use a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template. There are numberous different [templates](https://github.com/search?q=cookiecutter&type=Repositories) available
    The advantage of cookiecutter lies in their easy to use boilerplates that give a structured python project directory structure, ready to use files for version control, continuous integration (CI), licencing, and documentation.
    
    We recommend using either the cookiecutter for [computational molecular Science (CMS)](https://github.com/MolSSI/cookiecutter-cms) or the cookiecutter for [data science](https://drivendata.github.io/cookiecutter-data-science/#cookiecutter-data-science).
    Both have their advantages and disadvantages. If you are working with machine learning related projects, the data science cookiecutter might be better suited for you.

    You can install the CMS cookiecutter the following way:
    ```bash
    # If you don't have cookiecutter installed, you can install it with pip or conda
    conda install -c conda-forge cookiecutter
    # Create a new project with the CMS cookiecutter
    # There are several input options - if in doubt, use the default options
    cookiecutter gh:molssi/cookiecutter-cms
    ```

4. Version control system - github

    If you do not have git installed, follow the [instructions](https://git-scm.com/downloads) here.

    Then, if you do not have a github account yet, create an account [here](https://github.com/).
    As part of the MolInfo group, write us an email and we add you to your corresponding team.
    Afterwards you can push your own, local github project created with cookiecutter to the remote github location.
    To do this you can follow the instructions for [adding an existing project to GitHub using the command line](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git). Follow the first steps (1-3) to create a new repo within the MolInfo group on GitHub. From there, you can **skip point 4**, as the cookiecutter template initialized a local github repo already.
    Continue then with point 5.

    If you are doing research or making projects for any part of the MolInfo group, please create the repo there, not in your private account.
    Some best-practice for git usage can be found [here]().
    Moreover, when using our self-hosted [runners]() please only create private repos.

5. Documentation

6. Testing
    
    Testing can be done with many different frameworks. Using the CMS cookiecutter, `pytest` is integrated

7. Coding best practices

8. Deployment




    

    





