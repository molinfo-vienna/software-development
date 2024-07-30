"""Test module for the example module."""

import pytest
from project_xyz.example import add_numbers, Calculator


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


class TestCalculator:
    """Test suite for the Calculator class."""

    @pytest.fixture
    def calculator(self):
        """Fixture to create a Calculator instance."""
        return Calculator()

    def test_initial_result(self, calculator):
        """Test the initial result of the Calculator."""
        assert calculator.get_result() == 0

    def test_add(self, calculator):
        """Test the add method of the Calculator."""
        calculator.add(5)
        assert calculator.get_result() == 5
        calculator.add(3)
        assert calculator.get_result() == 8

    def test_add_negative(self, calculator):
        """Test adding negative numbers to the Calculator."""
        calculator.add(-5)
        assert calculator.get_result() == -5
        calculator.add(10)
        assert calculator.get_result() == 5