# Continuous Integration (CI)

Continuous Integration is the practice of automatically building and testing each change to your code frequently and automatically. This helps detect errors quickly and ensures that your changes don't break existing functionality.

## The Main Idea of CI

The core principle of CI is to have everyone working on a known stable base. Here are some key points:

* Commit code changes frequently (typically daily)
* Automate the build and test process
* Run tests on every commit
* Keep the build and test process fast
* Fix failing builds immediately

## Benefits of CI

* Early detection of integration issues
* Reduced time in debugging and fixing issues
* Improved code quality
* Faster release cycles

## Basic CI Workflow

1. Developer pushes code to the repository
2. CI server detects the change
3. CI server builds the project
4. CI server runs automated tests
5. CI server reports results to the team
6. If tests fail, the team fixes the issue immediately

## Implementing CI

While there are many CI services available, such as Travis CI and CircleCI, we recommend using GitHub Actions for projects hosted on GitHub. For a basic CI setup using GitHub Actions, create a file named `.github/workflows/ci.yml` in your repository:

```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: pytest
```

This simple workflow will run your tests on every push and pull request.

For more advanced CI setups, including linting, type checking, and deployment, refer to our [Advanced CI/CD with GitHub Actions guide](./ADVANCED_CI_CD.md).

## Template

Please also check out a working template [here](https://github.com/basf/cheminformatics_ci_cd_template)

__Next Chapter:__ [__IDE_Setup__](/IDE.md)
__Back:__ [__README__](/README.md)