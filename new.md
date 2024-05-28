
# Best Practices for Python Projects in the CD-Lab MIB

## Motivation for Adopting Best Practices in Coding
As PhD and Master’s students, you are often at the forefront of research and innovation, developing code that can lead to significant academic and technological advancements. By adopting the coding best practices outlined in this guide, you not only enhance the quality and maintainability of your projects but also dramatically increase their visibility within and beyond the academic community.

**Increased Job Prospects**: Employers in both academia and industry are increasingly valuing candidates who demonstrate a commitment to code quality and collaborative development practices. Showcasing well-maintained, clearly documented, and easily accessible projects on platforms like GitHub makes your work more discoverable and appealing to potential employers.

**Legacy and Reusability**: By following structured coding and documentation guidelines, your projects become easier for others to understand and build upon. This not only extends the lifespan of your code but also elevates your reputation as a researcher who contributes valuable, sustainable resources to the scientific community.

**Collaboration and Scalability**: Adopting these practices facilitates easier collaboration with other researchers, allowing your projects to scale and evolve. Well-documented code with thorough testing and packaging standards ensures that your software can be easily integrated and used in other projects, increasing its impact and relevance.

**Practical Learning and Skill Development**: Through the process of implementing these guidelines, you'll gain practical skills in software development that go beyond the academic environment. These skills are highly transferable and sought after in many career paths, providing a competitive edge in the job market.

In essence, by integrating these best practices into your development workflow, you're not just enhancing your current projects—you're setting a foundation for future success and recognition in your professional journey. This approach not only benefits your individual career but also contributes to the broader scientific community by fostering a culture of excellence and openness in research development.

This guide outlines essential practices for maintaining a high-quality Python codebase, including using linting, type hinting, documentation, and code analysis tools. It specifies integrating these tools with GitHub Actions, utilizing local runners.

## Linting (Code Style and Type Hinting)
- **Implement Linting Tools**: Utilize linting tools such as Flake8, Black, Bandit, Isort and Mypy to enforce coding standards and promote consistent code style across the project.
  - **Bandit**: Identifies potential security issues in Python code. `bandit -r --skip=B404,B603,B602 .`
  - **Black**: Formats code for consistent style, reducing the need for stylistic reviews. `black --check .`
  - **Flake8**: Analyzes code to catch syntax errors, bugs, and stylistic errors. `flake8 --extend-ignore=D203,E203,E501,W503 .`
  - **Isort**: Sorts imports alphabetically and automatically separates them into sections. `isort --profile black --check-only .`
  - **Mypy**: Checks and enforces type hints, improving code reliability and aiding in early detection of type-related errors. First install missing types: `mypy --install-types --non-interactive`. Then run mypy: `mypy --ignore-missing-imports --disallow-any-generics --disallow-untyped-defs --no-implicit-optional --disallow-incomplete-defs .`
  - **PyLint**: Another popular tool for enforcing coding standards and identifying potential issues. First install all required packages: `pip install $(find /app/linting/ -name "requirement*" -type f -printf ' -r %p')`. Then run PyLint on all files: `find . -type f -name "*.py" | xargs pylint -d C0301,R0913,W1202 --ignored-modules "rdkit"`
- **Implementation**: These tools should be configured to run in a GitHub Actions workflow using local runners to ensure that every commit adheres to established coding standards. To install these tools, use `pip install flake8 black bandit isort mypy pylint`.

## Documentation
- **Use Docstring Documentation**: Adhere to PEP 257 guidelines for docstring conventions, ensuring clear and consistent documentation throughout the codebase.
- **Automate Documentation Checks**: Integrate tools like Docsig, Interrogate, and Pydocstyle to automate documentation validation and enforce consistency.
  - **Docsig**: Checks that the docstring of a function matches its signature, ensuring consistency and accuracy. `docsig -C -D -m -N -o -p .`
  - **Interrogate**: Automates the validation of documentation against the code it documents, ensuring accuracy and completeness. `interrogate -O -vv .`
  - **Pydocstyle**: Enforces adherence to docstring conventions, enhancing code readability and maintainability. `pydocstyle .`
- **Parameter Definition and Documentation**: Every function parameter should be clearly defined with appropriate types and descriptive comments, enhancing maintainability and ease of use. The above tools can help enforce these practices. To install these tools, use `pip install docsig interrogate pydocstyle`.

## Testing Stage
- **Continuous Strive for High Test Coverage**: Maintain high test coverage across unit tests to ensure reliability and minimize regressions.
  - Tools like pytest and coverage.py should be configured to measure test effectiveness and coverage.
- **Implement Tests**: Write unit tests for all functions and classes, ensuring that each component behaves as expected under various conditions. Tests should be located within the repository under a `tests/` directory. Running all tests should be possible via `python -m unittest discover -v -s tests -p *.py -t .`.
- **Automate Testing**: Integrate the testing stage into you github actions to ensure that every commit is tested automatically.

## Packaging with PyPI
Packaging your Python project properly is crucial for distribution and reuse. Here's how to prepare and distribute your project via PyPI, the Python Package Index.

### Preparing Your Package
1. **Structure Your Project**: Organize your project files in a directory with a clear structure. Typically, this includes:
   - A `<module_name>/` directory where your package code resides.
   - A `tests/` directory for your unit tests.
   - Necessary files like `README.md`, `LICENSE`, `pyproject.toml`, and `requirements.txt`.

2. **Create a `pyproject.toml` File**: This script is essential for packaging your project. It should include metadata about your package like its name, version, author, and more. Dependencies listed in `requirements.txt` should be included under `install_requires` to ensure they are installed when your package is installed.
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

3. **Versioning**: Maintain clear versioning that adheres to semantic versioning standards. This helps users understand the extent of changes in each release.

### Distributing Your Package
For releasing your package on PyPI, follow this guide: https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/

## GitHub Actions Integration
All the above tools and practices should be integrated into a GitHub Actions workflow, ensuring they are automatically applied to every push or pull request. The following section (in a subsequent post) will provide a detailed example of the GitHub Actions YAML configuration file that implements these best practices using local runners. For further information, refer to the GitHub Actions documentation and [here](./GITHUB_ACTIONS.md).
