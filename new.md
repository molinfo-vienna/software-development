
# Best Practices for Python Projects in the CD-Lab MIB

## Motivation for Adopting Best Practices in Coding

### Enhance Code Visibility and Career Opportunities

As PhD and Master’s students, you are often at the forefront of research and innovation, developing code that can lead to significant academic and technological advancements. By adopting the coding best practices outlined in this guide, you not only enhance the quality and maintainability of your projects but also dramatically increase their visibility within and beyond the academic community.

**Increased Job Prospects**: Employers in both academia and industry are increasingly valuing candidates who demonstrate a commitment to code quality and collaborative development practices. Showcasing well-maintained, clearly documented, and easily accessible projects on platforms like GitHub makes your work more discoverable and appealing to potential employers.

**Legacy and Reusability**: By following structured coding and documentation guidelines, your projects become easier for others to understand and build upon. This not only extends the lifespan of your code but also elevates your reputation as a researcher who contributes valuable, sustainable resources to the scientific community.

**Collaboration and Scalability**: Adopting these practices facilitates easier collaboration with other researchers, allowing your projects to scale and evolve. Well-documented code with thorough testing and packaging standards ensures that your software can be easily integrated and used in other projects, increasing its impact and relevance.

**Practical Learning and Skill Development**: Through the process of implementing these guidelines, you'll gain practical skills in software development that go beyond the academic environment. These skills are highly transferable and sought after in many career paths, providing a competitive edge in the job market.

In essence, by integrating these best practices into your development workflow, you're not just enhancing your current projects—you're setting a foundation for future success and recognition in your professional journey. This approach not only benefits your individual career but also contributes to the broader scientific community by fostering a culture of excellence and openness in research development.

#####

This guide outlines essential practices for maintaining a high-quality Python codebase, including using linting, type hinting, documentation, and code analysis tools. It specifies integrating these tools with GitHub Actions, utilizing local runners.

## Linting and Code Style

- **Implement Linting Tools**: Utilize linting tools such as Flake8, Black, Bandit, and Isort to enforce coding standards and promote consistent code style across the project.
  - **Flake8**: Analyzes code to catch syntax errors, bugs, and stylistic errors.
  - **Black**: Formats code for consistent style, reducing the need for stylistic reviews.
  - **Bandit**: Identifies potential security issues in Python code.
  - **Isort**: Sorts imports alphabetically and automatically separates them into sections.
  - **Implementation**: These tools should be configured to run in a GitHub Actions workflow using local runners to ensure that every commit adheres to established coding standards.

## Type Hinting and Documentation

- **Enforce Type Hinting**: Use Mypy to enforce type hinting throughout the codebase.
  - **Mypy**: Checks and enforces type hints, improving code reliability and aiding in early detection of type-related errors.
- **Use PyDoc-Style Documentation**: Adhere to PyDoc conventions for documenting code functions and modules.
  - **DocSig Interrogate**: Automates the validation of documentation against the code it documents, ensuring accuracy and completeness.
- **Parameter Definition and Documentation**: Every function parameter should be clearly defined with appropriate types and descriptive comments, enhancing maintainability and ease of use.

## Code Analysis Tools

- **Utilize Code Analysis Tools**: Integrate tools such as SonarQube or Codacy to analyze code quality and maintainability.
  - These tools help detect issues, bugs, and code smells, offering insights into improving code quality.

## Testing Stage

- **Continuous Strive for High Test Coverage**: Maintain high test coverage across unit tests to ensure reliability and minimize regressions.
  - Tools like pytest and coverage.py should be configured to measure test effectiveness and coverage.

## GitHub Actions Integration

All the above tools and practices should be integrated into a GitHub Actions workflow, ensuring they are automatically applied to every push or pull request. The following section (in a subsequent post) will provide a detailed example of the GitHub Actions YAML configuration file that implements these best practices using local runners.

---

This framework sets a structured approach to code quality and consistency, essential for collaborative projects. The next step will be to provide an example YAML file to showcase how to set up and execute these practices within a GitHub Actions workflow.

## Packaging with PyPI

Packaging your Python project properly is crucial for distribution and reuse. Here's how to prepare and distribute your project via PyPI, the Python Package Index.

### Preparing Your Package

1. **Structure Your Project**: Organize your project files in a directory with a clear structure. Typically, this includes:
   - A `src/` directory where your package code resides.
   - A `tests/` directory for your unit tests.
   - Necessary files like `README.md`, `LICENSE`, `setup.py`, and `requirements.txt`.

2. **Create a `setup.py` File**: This script is essential for packaging your project. It should include metadata about your package like its name, version, author, and more. Dependencies listed in `requirements.txt` should be included under `install_requires` to ensure they are installed when your package is installed.

   ```python
   from setuptools import setup, find_packages

   setup(
       name='your_package_name',
       version='0.1.0',
       packages=find_packages(where="src"),
       package_dir={"": "src"},
       install_requires=[
           'numpy',  # Example dependency, specify your project's dependencies here
           'requests'
       ],
       # Additional metadata like author, classifiers, etc.
   )
   ```

3. **Include a `MANIFEST.in`**: This file tells Python what files to include in the distribution package besides the ones in `setup.py`.

   ```
   include LICENSE
   include README.md
   recursive-include data *
   ```

4. **Versioning**: Maintain clear versioning that adheres to semantic versioning standards. This helps users understand the extent of changes in each release.

### Distributing Your Package

1. **Build Your Package**: Use the following command to generate distribution archives for the package.
   ```bash
   python setup.py sdist bdist_wheel
   ```

2. **Upload to PyPI**: Use Twine to upload your package to PyPI. First, install Twine via pip:
   ```bash
   pip install twine
   ```
   Then, run Twine to upload your distribution archives:
   ```bash
   twine upload dist/*
   ```

3. **Maintain Your Package**: Keep your package updated with bug fixes, improvements, and compatibility with dependencies and Python versions. Use version tagging and GitHub releases to manage these updates transparently.

### Integration with GitHub Actions

Include steps in your GitHub Actions workflow to automate testing, building, and deploying your package to PyPI. This ensures that every release meets quality standards and simplifies the release process. In the next section, we will provide a detailed example of the GitHub Actions YAML configuration file that accomplishes this integration along with the previous best practices.


## GitHub Actions Workflow Example

Here's an example YAML configuration file for GitHub Actions, demonstrating how to incorporate linting, testing, type hinting, and packaging for a Python project. This file also shows how to automate the deployment of the package to PyPI using local runners.

```yaml
name: Python Package CI/CD

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build-and-test:
    runs-on: self-hosted
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest pytest-cov mypy black bandit isort twine
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        
    - name: Lint with Flake8
      run: flake8 src/ tests/
      
    - name: Check import order with Isort
      run: isort --check-only src/ tests/
      
    - name: Format code with Black
      run: black --check src/ tests/
      
    - name: Security check with Bandit
      run: bandit -r src/
      
    - name: Type check with Mypy
      run: mypy src/
      
    - name: Run pytest
      run: pytest --cov=src tests/
      
    - name: Build package
      run: python setup.py sdist bdist_wheel
      
    - name: Publish to PyPI
      if: github.ref == 'refs/heads/main' && github.event_name == 'push'
      run: twine upload dist/*
      env:
        TWINE_USERNAME: ${{ secrets.PYPI_USERNAME }}
        TWINE_PASSWORD: ${{ secrets.PYPI_PASSWORD }}

```

### Explanation of the Workflow

- **Trigger**: The workflow is triggered on push or pull requests to the `main` branch.
- **Build and Test Job**: This job uses a self-hosted runner.
  - **Checkout**: The current repository code is checked out.
  - **Set up Python**: Python 3.8 is set up for use in the runner.
  - **Install dependencies**: Essential tools and project-specific dependencies are installed.
  - **Linting and Formatting**: Flake8, Isort, and Black are used to ensure code quality and style.
  - **Security Checks**: Bandit performs a static analysis for security vulnerabilities.
  - **Type Checking**: Mypy checks for type consistency.
  - **Testing**: Pytest runs tests and measures code coverage.
  - **Build Package**: The project is packaged into distributable formats.
  - **Publish to PyPI**: If conditions are met (push to main branch), the package is uploaded to PyPI using Twine.

### Running the Workflow

To run this workflow, simply push changes to your `main` branch or create a pull request against it. The workflow will execute automatically, ensuring your code adheres to quality standards and is packaged correctly for distribution. Ensure that PyPI credentials (`PYPI_USERNAME` and `PYPI_PASSWORD`) are securely stored in your GitHub repository's secrets.

This comprehensive approach leverages GitHub Actions with local runners to maintain high standards in your Python project, automating testing, linting, security checks, type checking, and deployment to PyPI.