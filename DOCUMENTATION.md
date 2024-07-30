# Documentation

Proper documentation is crucial for the usability and maintainability of your project. Start documenting as early as possible in your development process.

## README.md

Your README.md should include:

- What your project can do
- How to install it
- Requirements
- How to use it
- License information
- Where to ask questions

## Docstrings

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

## Tools for Documentation

- **Sphinx**: A powerful documentation generator. It's especially useful for larger projects.
- **GitHub Wiki**: An easy-to-use option for smaller projects or getting started with documentation.


__Next Chapter:__ [__LINTING__](/LINTING.md)
__Back:__ [__README__](/README.md)