# Project Structure

Giving structure to your project is of utmost importance - no matter what you're doing. A well-organized project structure enhances readability, maintainability, and collaboration.

## Template

Please also check out a working template [here](https://github.com/basf/cheminformatics_ci_cd_template)

## Basic Project Structure

A typical Python project structure might look like this:

```
project/
    docs/
    project_name/
        __init__.py
        main.py
    tests/
        __init__.py
        test_main.py
    .gitignore
    LICENSE
    README.md
    requirements.txt
    setup.py
```

## Key Components

### Root Directory

The root directory should contain:

- `LICENSE`: Specifies how others can use your code.
- `README.md`: Provides an overview of your project, installation instructions, and basic usage. 
- `setup.py`: Used for packaging and distributing your project. More can be read about [here](/SETUP.md).
- `.gitignore`: Tells Git which files to ignore. More can be read about [here](/GITIGNORE.md).
- `requirements.txt`: Lists the project dependencies. More can be read about [here](/REQU.md).

### Source Code Directory (`project_name/`)

Place your main package code here. This separation helps prevent import issues and clearly distinguishes your package code from other project files.

### Tests Directory (`tests/`)

Contains all your test files. Keeping tests separate from your source code is a best practice.

### Documentation (`docs/`)

Store your project documentation here. Consider using tools like Sphinx for generating comprehensive documentation.

### ___init___.py

More can be read about [here](/INIT.md)

## Using Cookiecutter Templates

We recommend using a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template to set up your project structure. This tool provides ready-to-use boilerplates with a structured directory layout and essential files for version control, continuous integration, licensing, and documentation.

For molecular informatics projects, we suggest:

1. [Computational Molecular Science (CMS) Cookiecutter](https://github.com/MolSSI/cookiecutter-cms)
2. [Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/)

To use the CMS cookiecutter:

```bash
# Install cookiecutter
pip install cookiecutter

# Create a new project
cookiecutter gh:molssi/cookiecutter-cms
```

## Best Practices

1. Keep your project structure consistent across all your projects.
2. Use meaningful names for directories and files.
3. Separate your code into logical modules.
4. Keep your root directory clean; most of your code should be in the `src/` directory.
5. Use virtual environments to manage project dependencies.

By following these guidelines, you'll create a clean, organized project structure that's easy to navigate and maintain.

__Next Chapter:__ [__Documentation__](/DOCUMENTATION.md)
__Back:__ [__README__](/README.md)