This setup guide is for everyone wanting to set up a molecular informatics project in python project quickly and easily.
In order to maximize collaborations and reusability of each project, we recommend making a package out of your project.
This allows for easy access to your code, reduces the time to implement new features, and collaborate with others. 
If you are working on sensitive topics that should not be public, you do not have to deploy to [Conda](https://anaconda.org/) or [PyPI](https://pypi.org/).

1. Get a proper IDE

    We recommend downloading and installing <mark>VS Code</mark> for your project.
    There are numerous other IDEs (e.g. PyChamr, Spyer,...) but VS Code is lightweight and can be extended easily to the favor of your choice.

    To download and install our recommendation go to [VS Code Homepage](https://code.visualstudio.com/download). Follow the instructions for your operating system.


2. Setup your python package manager

    The standard python package manager is [pip](https://pypi.org/project/pip/). It is built-in to python and can install a huge variety of packages from different sources. It installs packages into a project's global python environment and is accessed by all projects.
    As soon as you need to manage different versions of particular packages that might interfere with other package dependencies, conflicts may arise.

    For this and other reasons we recommend using [conda](https://docs.conda.io/projects/conda/en/latest/) as the main python package manager. It allows to create virtual environments with different versions of packages.
    If packages are not available, use pip to install them into the global environment.
    We encourage the use of different environments for different projects. 
    Therefore make it easy for collaborators to set up the same environment without caring too much about dependencies.

    Conda can be downloaded for your operating system [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Follow the instructions given and save it at a convenient location ("/path/to/miniconda/").

    After the installation process is finished, create a new environment with a fitting and easy-to-remember name as you need to activate it frequently.

    **Local installation**
    When working with your own code as a package and you want to reference it locally, it is often recommended to do a "local" python install via ```pip install -e .``` - this works only if you are in the root folder of your package. This command will insert your new project into your Python site-packages folder so that it can be found in any directory on your computer.
    
3. Structure your project

    Giving structure to your project is of uttermost importance - no matter what you are doing.

    There are many ways how to structure your python software project - be it on your own or via a template.

    In general, a good practice is to separate the various elements of your software project into separate locations within the project. 
    A software project is not just the code needed to perform its tasks, but also to document and deploy.

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
        .gitignore
    ```

    ***root directory***

    Primary setup file and Git(Hub) Helpers 

    ```
    LICENSE.md
    README.md
    setup.py
    .gitignore
    ```

    The root directory should contain the primary `setup.py` file for the `examplepackage`. This is the primary file that
    users and deployment tools will run to build the package. This is a
    [critical component of any Python package][https://docs.python.org/3/distutils/setupscript.html] and should always be included.

    The three files, `LICENSE.md`, `README.md`, and `.gitignore` are Git and GitHub-specific files that should always be included. The `LICENSE.md` file is a direct copy of the [licensing] the package falls under. GitHub can detect the most common licenses from this file automatically and add the front page of the
    project with this information (as shown in the red box in the image below).

    ![The license file is automatically detected by GitHub][license_highlight]

    The `README.md` file is the *most important file* for a GitHub project. A Markdown file with this name is rendered
    by GitHub on the project's homepage. That means this is the **FIRST** thing users see when visiting `exampleproject`,
    so this should be an informative file that tells users the following:
    1. Short explanation of what the project does
    1. Quick "How-To install and run" the project. This should be only a few lines, which is why its important to
    ensure the project can be installed easily.
    * This topic is covered [in a later chapter][package_deploy_page], but it is important to plan for this section now
    1. Who are the authors of the package are
    1. Where to read the full documentation

    The `README.md` is not the place to dump all the documentation for the package for most packages, but it should
    inform the users how to access all the needed info. More info on good `README.md` files can be found
    [in a later chapter][documentation_page].

    The final file in the root directory is the `.gitignore` file which tells `git` (not GitHub) file patterns to ignore
    when adding files to the repository, one per line. This helps prevent accidental file additions such as
    compiled Python binaries `.pyc` files with the simple pattern `*.pyc`. There is no "master" list for every project,
    but [GitHub has some handy templates][gitignore_template] packages can borrow. This is not a required file but will
    make software development much easier by reducing the number of accidental file commits.


    *** Licencing ***
    The license terms are of uttermost importance but often overlooked.
    Without explicitly specifying a license that describes how your work may be used, you may inadvertently greatly limit the impact of your work because copyright and related laws restrict how others can use it.

    Two categories of licenses can be defined:

    * [__Permissive__](https://en.wikipedia.org/wiki/Permissive_software_licence): Places no restriction on the use of the code in derivative works, including commercialization. Often only requires citation.

    * [__Copyleft__](https://en.wikipedia.org/wiki/Copyleft): Requires that derivative works also be open source.

    It is also important to remember that different licenses may not be compatible with each other. For instance, if you use a "copyleft" licensed codebase to develop your codebase, you may not be able to use a permissive license.
    
    **It is also critical to note that having an open source license does not preclude dual licensing, allowing authors to distribute the code under different licenses to different parties.**
    Issuing a second license generally requires the approval of all authors, so can be a complex issue (see Relicensing below).

    For more details look at the [Licencing](https://github.com/molinfo-vienna/wiki/blob/additional_readme/LICENCING.md) file.

    **Cookiecutter**

    We recommend using a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template. There are numerous different [templates](https://github.com/search?q=cookiecutter&type=Repositories) available
    The advantage of cookiecutter lies in their easy-to-use boilerplates that give a structured python project directory structure, ready-to-use files for version control, continuous integration (CI), licensing, and documentation.
    
    We recommend using either the cookiecutter for [computational molecular Science (CMS)](https://github.com/MolSSI/cookiecutter-cms) or the cookiecutter for [data science](https://drivendata.github.io/cookiecutter-data-science/#cookiecutter-data-science).
    Both have their advantages and disadvantages. If you are working with machine-learning related projects, the data science cookiecutter might be better suited for you.

    You can install the CMS cookiecutter the following way:
    ```bash
    # If you don't have cookiecutter installed, you can install it with pip or conda
    conda install -c conda-forge cookiecutter
    # Create a new project with the CMS cookiecutter
    # There are several input options - if in doubt, use the default options
    cookiecutter gh:molssi/cookiecutter-cms
    ```


4. Version control system - GitHub

    If you do not have git installed, follow the [instructions](https://git-scm.com/downloads) here.

    Then, if you do not have a GitHub account yet, create an account [here](https://github.com/).
    As part of the MolInfo group, write us an email and we add you to your corresponding team.
    Afterward, you can push your own, local GitHub project created with cookiecutter to the remote GitHub location.
    To do this you can follow the instructions for [adding an existing project to GitHub using the command line](https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git). Follow the first steps (1-3) to create a new repo within the MolInfo group on GitHub. From there, you can **skip point 4**, as the cookiecutter template initialized a local GitHub repo already.
    Continue then with point 5.

    If you are doing research or making projects for any part of the MolInfo group, please create the repo there, not in your private account.
    Some best-practice for git usage can be found [here]().
    Moreover, when using our self-hosted [runners]() please only create private repos.

    In general, one should 

5. Documentation

6. Testing
    
    Testing can be done with many different frameworks. Using the CMS cookiecutter, `pytest` is integrated

7. Coding best practices



8. Deployment



    





