# Project XYZ Template

This is a template for Project XYZ that follows good Python practices. Follow the [good practices](/README.md).

## Minimum Requirements

1. Use the specified linters: isort, black, and pylint.
2. Use the specified documentation check with pydocstyle.
3. Ensure test coverage is above 80%.
4. Distribute your library as a package.

## Folder Structure

```
project_template/
├── src/
│   └── project_xyz/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── pyproject.toml
├── setup.cfg
├── README.md
└── requirements.txt
```

Check out the details about [gitignore](/GITIGNORE.md), [pyproject.toml](/PROJECT_TOML.md), [setup.cfg](/SETUP.md), [__init__.py](/INIT.md), and [requirement.txt](/REQU.md)

## Setup

1. Copy this template to your project directory.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Customize the `pyproject.toml` and `setup.cfg` files with your project-specific information.

## Usage

### Local Development

#### Linting

To run the linters locally, use the following commands:

```bash
isort .
black .
pylint src tests
```

#### Documentation Check

To check the documentation style locally, run:

```bash
pydocstyle src
```

#### Testing

To run tests and generate a coverage report locally, use:

```bash
pytest
```

You can also use [VS Code test suite](https://code.visualstudio.com/docs/python/testing)

### Continuous Integration with GitHub Actions

This template includes a GitHub Actions workflow for continuous integration. When you push to the main branch or create a pull request, it automatically runs linting, testing, and other checks.

The workflow is defined in `.github/workflows/ci.yml` and includes the following steps:

1. Linting with isort, black, and pylint
2. Documentation style check with pydocstyle
3. Running tests with pytest and generating a coverage report
4. Building the package

To enable this workflow:

1. Ensure the `.github/workflows/ci.yml` file is present in your repository.
2. Push your changes to GitHub.
3. Go to the "Actions" tab in your GitHub repository to see the workflow runs.

You can customize the workflow by editing the `.github/workflows/ci.yml` file.

### VS Code Integration

For local development in VS Code, you can set up linting and formatting to run automatically:

1. Install the Python extension for VS Code.
2. Open your project in VS Code.
3. Go to Settings (Ctrl+,) and search for "Python Linting".
4. Enable pylint, and set it as the default linter.
5. In the same settings, enable formatOnSave and set Black as the default formatter.

This setup will run linting and formatting automatically as you work on your code in VS Code.

### Packaging

To build your package, run:

```bash
python -m build
```

## Project Structure

- `src/project_xyz/`: Main package source code
  - `__init__.py`: Package initialization file
  - `example.py`: Example module with sample code
- `tests/`: Test files
  - `__init__.py`: Test package initialization file
  - `test_example.py`: Test file for the example module
- `.github/workflows/`: GitHub Actions workflow definitions
- `.gitignore`: Git ignore file
- `pyproject.toml`: Project configuration file
- `setup.cfg`: Setup configuration file
- `README.md`: Project documentation
- `requirements.txt`: Project dependencies

## Further Reading

For more information, refer to the following sections:
- [CI/CD Guidelines](./CI.md)
- [Advanced Techniques](./ADVANCED_CI_CD.md)
- [Linting](./LINTING.md)
- [Good Documentation Practices](./DOCUMENTATION.md)