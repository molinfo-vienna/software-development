# Documentation and Linting

## Documentation

Proper documentation is crucial for the usability and maintainability of your project. Start documenting as early as possible in your development process.

### README.md

Your README.md should include:

- What your project can do
- How to install it
- Requirements
- How to use it
- License information
- Where to ask questions

### Docstrings

Use docstrings to document classes, methods, and functions. Follow the PEP 257 guidelines for consistency.

Example of a well-documented function:

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width
```

### Tools for Documentation

- **Sphinx**: A powerful documentation generator. It's especially useful for larger projects.
- **GitHub Wiki**: An easy-to-use option for smaller projects or getting started with documentation.

## Linting

Linting helps maintain code quality by checking for potential errors and style inconsistencies.

### Basic Linting Setup

1. Install a linter (e.g., flake8):
   ```
   pip install flake8
   ```

2. Run the linter:
   ```
   flake8 your_project_directory
   ```

3. Integrate with your text editor or IDE for real-time linting.

### Example of Linting Issues

```python
# Bad: Inconsistent indentation and unused import
import sys

def badfunction( x ):
    y = x + 1
        return y  # Indentation error

# Good: Corrected version
def good_function(x):
    return x + 1
```

For more advanced linting setup, including integration with GitHub Actions, refer to our [GitHub Actions guide](./GITHUB_ACTIONS.md).

## Type Hinting

Type hinting improves code readability and helps catch type-related errors early.

### Basic Type Hinting

```python
from typing import List, Dict, Optional

def process_data(data: List[Dict[str, int]], factor: Optional[float] = None) -> List[float]:
    """
    Process a list of dictionaries containing integer values.

    Args:
        data (List[Dict[str, int]]): A list of dictionaries with string keys and integer values.
        factor (Optional[float]): A multiplication factor. Defaults to None.

    Returns:
        List[float]: A list of processed values.
    """
    result: List[float] = []
    for item in data:
        for value in item.values():
            processed_value = float(value)
            if factor is not None:
                processed_value *= factor
            result.append(processed_value)
    return result

# Usage
sample_data: List[Dict[str, int]] = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
processed_result: List[float] = process_data(sample_data, factor=1.5)
print(processed_result)  # Output: [1.5, 3.0, 4.5, 6.0]
```

### Type Checking

Use a tool like `mypy` to check for type consistency:

```
pip install mypy
mypy your_script.py
```

## Best Practices

1. Document as you code, don't leave it for later.
2. Use consistent formatting in your documentation.
3. Run linters and type checkers regularly, ideally as part of your development workflow.
4. Keep your documentation up-to-date as your code evolves.

For more detailed information on documentation tools and advanced linting setups, refer to our [GitHub Actions guide](./GITHUB_ACTIONS.md).

Next Chapter: [Packaging and Continuous Deployment](./PACKAGING.md)