# Advanced CI/CD with GitHub Actions

This guide combines advanced Continuous Integration (CI) and Continuous Deployment (CD) practices using GitHub Actions.

## Comprehensive GitHub Actions Workflow

Here's an example of a more comprehensive GitHub Actions workflow that includes testing, linting, type checking, and deployment:

```yaml
name: CI/CD

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest mypy black isort
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    
    - name: Lint with flake8
      run: flake8 .
    
    - name: Check imports with isort
      run: isort --check-only .
    
    - name: Format with Black
      run: black --check .
    
    - name: Type check with mypy
      run: mypy .
    
    - name: Run tests
      run: pytest
    
    - name: Build package
      run: python setup.py sdist bdist_wheel
    
    - name: Publish to PyPI
      if: github.event_name == 'push' && github.ref == 'refs/heads/main'
      uses: pypa/gh-action-pypi-publish@release/v1
      with:
        user: __token__
        password: ${{ secrets.PYPI_API_TOKEN }}
```

This workflow does the following:

1. Runs on every push to main and every pull request to main
2. Sets up Python 3.8
3. Installs dependencies
4. Runs linting with flake8
5. Checks import order with isort
6. Checks formatting with Black
7. Runs type checking with mypy
8. Runs tests with pytest
9. Builds the package
10. Publishes to PyPI if the event is a push to main

## Noteworthy comments

The most important tools are:

* pylint
* pydocstyle
* coverage
* black
* isort

`Black` and isort come basically for free, since they only re-formart your code.

`pylint` is probably the most comprehensive linter and should catch most linting problems.

`pydocstyle` helps to have consistent doc-string throughout the project.

The test coverage from the `coverage` package can give very valuable insides while developing/writing test and is a quality measure for a project. Also, a minimum threshold for code coverage can be set in the CI/CD pipeline to ensure high coverage.

A project passing a CI/CD template with these packages is already a trustworthy project.

## Customizing the Workflow

You can customize this workflow based on your project's needs. For example:

* Add multiple Python versions for testing
* Include coverage reporting
* Add deployment steps for different environments (staging, production)
* Integrate with other services (e.g., Docker, AWS)

### CI/CD services

There are many CI/CD services out there — such as [GitHub Actions](https://docs.github.com/en/actions), [Travis CI](https://www.travis-ci.com/), and [CircleCi](https://circleci.com/). 
We recommend using GitHub Actions, which is a service for executing CI/CD workflows for software stored in a GitHub repository.
Github Actions offers integrated [CI](https://docs.github.com/en/actions/deployment/about-deployments/about-continuous-deployment) and [CD](https://docs.github.com/en/actions/deployment/about-deployments/about-continuous-deployment) workflows.

In order to get to know GitHub Actions we recommend the official [Understand GitHub Actions homepage](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) as well as the [building and testing python code](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) GitHub Actions site.
Another good resource is the [Python Packages homepage](https://py-pkgs.org/08-ci-cd.html) for more details, key concepts, and examples.

One important note is that when using self hosted runners `ALWAYS` use private repos! Please read the security concerns [here](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners#self-hosted-runner-security).

We provide self hosted runners for GitHub Actions CI/CD - the how to use them can be found [here](https://github.com/molinfo-vienna/software-development/blob/main/ADMINISTRATION.md#server-usage-and-self-hosted-runners)

## Best Practices for CI/CD

1. Keep your CI/CD pipeline fast
2. Use caching to speed up builds
3. Only run comprehensive tests on main branch and pull requests
4. Use environment variables and secrets for sensitive information
5. Use status checks to prevent merging broken code
6. Regularly update your dependencies and GitHub Actions versions

By implementing these advanced CI/CD practices, you can ensure high code quality, catch issues early, and streamline your deployment process.

For more information on GitHub Actions, refer to the [official documentation](https://docs.github.com/en/actions).

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

__Next Chapter:__ [__Licencing__](/LICENCING.md)
__Back:__ [__README__](/README.md)