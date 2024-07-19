## Introduction to Linting, Type Hinting, and Code Style in Python

This is a minimum requirement for your projects working together in the CD-MIB (Another requirement can be found in the following sections: [CI](/CI.md), [testing](/TEST.md), [advance CI](/ADVANCED_CI_CD.md)).

In the world of software development, maintaining readability, consistency, and error-free code are paramount. This is where the practices of linting, type hinting, and adhering to a code style come into play, especially in dynamic programming languages like Python. These practices not only enhance code quality and maintainability but also streamline collaboration across large teams. Let's delve into what each of these terms means and why they are crucial for writing good Python code.

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

Look at an automated example [here](/ADVANCED_CI_CD.md##Comprehensive GitHub Actions Workflow) that includes linting tools and a GitHub Actions workflow.