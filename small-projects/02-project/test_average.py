"""
    Function Definition: Write a function called calculate_average that takes a list of numbers as input and returns the average of the numbers. Include a check to handle the case where the list is empty (return 0 in that case).
Testing with pytest: Create a file named test_average.py. Write at least three test functions to test the calculate_average function:

    Test with a list of positive numbers.
    Test with a list containing zero.
    Test with an empty list.


"""

import pytest
from average import calculate_average


def test_calculate_average_positive():
    """Test with a list of positive numbers."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0


def test_calculate_average_mixed():
    """Test with a list containing zero and positive numbers."""
    assert calculate_average([0, 1, 2, 3, 4, 5]) == 2.5


def test_calculate_average_negative():
    """Test with a list of negative numbers."""
    assert calculate_average([-1, -2, -3, -4, -5]) == -3.0  # Corrected assertion


def test_calculate_average_empty():
    """Test with an empty list."""
    assert calculate_average([]) == 0
