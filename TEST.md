# Testing

Writing tests while developing your code is a good practice that makes your code more reliable and less prone to failures or bugs. Testing can be done with various frameworks, but we'll focus on pytest, which is integrated with the CMS cookiecutter.

## Unit Testing

When writing tests, keep the following in mind:

* Each test unit should focus on a small functionality and prove it correct
* Each new functionality should be covered by a unit test
* Each test unit should be independent of others
* Make each test unit run fast and avoid unnecessary, complex structures
* Each test unit should be run automatically on push operations
* Run your whole test suite before and after your work to check whether you introduced an error
* Use descriptive names for your test units
* A test unit without purpose should be avoided
* When collaborating, looking at and running unit tests can be helpful to understand the code

## Getting Started with pytest

To get started with pytest, first install it:

```bash
pip install pytest
```

Here's a simple example of a test using pytest:

```python
# In file test_example.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
```

Run your tests using:

```bash
pytest
```

## Test Coverage

To ensure your tests are comprehensive, you can use a tool like coverage.py to measure test coverage:

```bash
pip install coverage
coverage run -m pytest
coverage report
```

This will show you which parts of your code are covered by tests and which are not.

For more advanced testing setups, including integration with CI systems, refer to our [Continuous Integration guide](./CI.md).

__Next Chapter:__ [__Continuous_Integration__](/CI.md)
__Back:__ [__README__](/README.md)