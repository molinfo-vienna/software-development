
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

### Running the Workflow

To run this workflow, simply push changes to your `main` branch or create a pull request against it. The workflow will execute automatically, ensuring your code adheres to quality standards and is packaged correctly for distribution. Ensure that PyPI credentials (`PYPI_USERNAME` and `PYPI_PASSWORD`) are securely stored in your GitHub repository's secrets.

This comprehensive approach leverages GitHub Actions with local runners to maintain high standards in your Python project, automating testing, linting, security checks, type checking, and deployment to PyPI.

Let's break down the provided GitHub Actions workflow example for a Python project into more detailed steps. This should help new users understand how each part functions and what they might need to adjust based on their project's requirements.

### Detailed Explanation of Each Step in the Workflow:

1. **Workflow Triggers**:
   - **`on: push:`** and **`on: pull_request:`** specify that the workflow should start either when commits are pushed to the `main` branch or when a pull request is made to the `main` branch. This ensures that any code changes are automatically tested and deployed if they meet the specified conditions.

2. **Jobs - Build and Test**:
   - **`runs-on: self-hosted`**: This line specifies that the workflow should run on a self-hosted runner, not on GitHub's hosted runners. This means you must have a runner set up in your environment, which can be beneficial for performance, security, or usage of internal resources.

3. **Steps within the Job**:
   - **`actions/checkout@v2`**: This action checks out your repository under `$GITHUB_WORKSPACE`, so your workflow can access it.
   - **`actions/setup-python@v2`**: Sets up a Python environment using Python 3.8. It's essential for Python-based projects to specify which Python version they are using to avoid compatibility issues.

4. **Dependency Installation**:
   - **Installing tools and packages**: The script upgrades `pip` and installs several packages (`flake8`, `pytest`, etc.) which are necessary for linting, testing, and other checks. 
   - **Project-specific dependencies**: If a `requirements.txt` file exists, it installs additional dependencies from there, which are specific to your project.

5. **Quality Assurance and Testing Steps**:
   - **Linting with Flake8**: Checks the code for style issues and programming errors.
   - **Checking import order with Isort**: Ensures that import statements are clean and sorted in a standard format.
   - **Code formatting with Black**: Validates that the code follows the uncompromising code style.
   - **Security checks with Bandit**: Scans code for common security issues.
   - **Type checking with Mypy**: Verifies type hints and type usage throughout the codebase.
   - **Running tests with pytest**: Executes unit tests and generates a coverage report to ensure functionality works as expected.

6. **Building the Package**:
   - **`python setup.py sdist bdist_wheel`**: This command packages the project into a source distribution and a wheel. These files are what you would upload to a package index like PyPI.

7. **Conditional Deployment**:
   - **Publish to PyPI**: If the previous steps are successful and the push is made to the `main` branch, the workflow uses `twine` to upload the package to PyPI. This step uses environment variables (`TWINE_USERNAME` and `TWINE_PASSWORD`) stored in GitHub Secrets to securely authenticate to PyPI.

### Running the Workflow:

To make this workflow operational, push changes to your `main` branch or create a pull request against it. Ensure you have set up the necessary Python environment and have GitHub Secrets configured with your PyPI credentials for deployment.

### Customization Tips for New Users:

- **Python Version**: Adjust the `python-version` in the `setup-python` step according to your project’s requirements.
- **Dependencies**: Modify the list of installed tools in the dependency installation step based on your coding and testing practices.
- **Additional Testing or Building Steps**: You can add more steps, such as integration testing or Docker containerization, depending on your project’s complexity and deployment needs.
- **Environment Variables and Secrets**: Make sure you configure the required secrets in your GitHub repository settings to handle credentials safely.

By understanding each part of this workflow, you can effectively maintain high standards in your project, automating various checks and deployments efficiently.

### GitHub Copilot: An Overview

#### What is GitHub Copilot?

GitHub Copilot is an AI-powered code completion tool developed by GitHub and OpenAI. It functions as a virtual coding assistant that suggests entire lines or blocks of code as you type, helping to streamline the coding process. Copilot is designed to understand context from the code you're writing, offering not just simple completions but also complex code snippets based on its understanding of numerous programming languages and frameworks.

#### Benefits for Students

For students, GitHub Copilot can be an invaluable tool. It aids in learning by providing suggestions and examples, making it easier to understand new programming concepts and languages. Moreover, Copilot can boost productivity and encourage best practices by suggesting modern or more efficient coding methods.

#### How to Sign Up for GitHub Copilot as a Student

As a student, you can access GitHub Copilot typically through the GitHub Student Developer Pack, which includes a variety of free tools and services intended for educational purposes. Here’s a quick guide on how to sign up:

1. **Verify Your Student Status**: Go to GitHub’s Student Developer Pack page and apply for the pack by providing verification of your enrollment at a degree-granting university or college.
2. **Access GitHub Copilot**: Once your student status is verified, and you have access to the Developer Pack, you can activate GitHub Copilot as part of your GitHub account.

#### Installing GitHub Copilot in Visual Studio Code

Installing GitHub Copilot in VS Code is straightforward:

1. **Open Visual Studio Code**: Start by opening your VS Code editor.
2. **Access the Extensions Marketplace**: Click on the Extensions view icon on the Sidebar or press `Ctrl+Shift+X`.
3. **Search for GitHub Copilot**: Type "GitHub Copilot" into the search bar in the Extensions view.
4. **Install the Extension**: Find the GitHub Copilot extension in the list and click the install button. After installation, you’ll be prompted to sign in with your GitHub account to activate the extension.

#### Using GitHub Copilot Effectively

Here are a few tips on how to make the most out of GitHub Copilot:

- **Explore Code Alternatives**: Use Copilot’s suggestions to explore different ways to implement functionality and learn from the diverse coding styles and approaches it provides.
- **Understand the Suggestions**: While Copilot can generate code quickly, take the time to understand what the suggested code does before incorporating it into your project.
- **Refine and Customize**: Copilot's suggestions may not always be perfect. Use them as a starting point and refine them to fit your specific requirements and coding standards.

GitHub Copilot is particularly useful for writing boilerplate code, exploring new libraries and frameworks, and learning best practices in software development. As you use Copilot, you'll likely find that it not only helps you code more efficiently but also educates you on different aspects of programming and software development.