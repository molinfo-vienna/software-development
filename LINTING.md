## Linting (Code Style and Type Hinting)
- **Implement Linting Tools**: Utilize linting tools such as Flake8, Black, Bandit, Isort and Mypy to enforce coding standards and promote consistent code style across the project.
  - **Bandit**: Identifies potential security issues in Python code. `bandit -r --skip=B404,B603,B602 .`
  - **Black**: Formats code for consistent style, reducing the need for stylistic reviews. `black --check .`
  - **Flake8**: Analyzes code to catch syntax errors, bugs, and stylistic errors. `flake8 --extend-ignore=D203,E203,E501,W503 .`
  - **Isort**: Sorts imports alphabetically and automatically separates them into sections. `isort --profile black --check-only .`
  - **Mypy**: Checks and enforces type hints, improving code reliability and aiding in early detection of type-related errors. First install missing types: `mypy --install-types --non-interactive`. Then run mypy: `mypy --ignore-missing-imports --disallow-any-generics --disallow-untyped-defs --no-implicit-optional --disallow-incomplete-defs .`
  - **PyLint**: Another popular tool for enforcing coding standards and identifying potential issues. First install all required packages: `pip install $(find /app/linting/ -name "requirement*" -type f -printf ' -r %p')`. Then run PyLint on all files: `find . -type f -name "*.py" | xargs pylint -d C0301,R0913,W1202 --ignored-modules "rdkit"`
- **Implementation**: These tools should be configured to run in a GitHub Actions workflow using local runners to ensure that every commit adheres to established coding standards. To install these tools, use `pip install flake8 black bandit isort mypy pylint`.

