"""Example module for Project XYZ."""

def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers and return the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b


class Calculator:
    """A simple calculator class."""

    def __init__(self):
        """Initialize the Calculator instance."""
        self.result = 0

    def add(self, number: int) -> None:
        """
        Add a number to the current result.

        Args:
            number (int): The number to add.
        """
        self.result += number

    def get_result(self) -> int:
        """
        Get the current result.

        Returns:
            int: The current result.
        """
        return self.result