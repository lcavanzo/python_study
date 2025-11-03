# test_rectangle.py
"""
Testing: Create a corresponding test file (test_geometry.py) and write a comprehensive suite of unit tests for this function. Consider:

    Positive dimensions.
    Zero dimensions (area should be 0).
    Negative dimensions (should raise a ValueError with an appropriate message, e.g., "Dimensions cannot be negative.").
    Floating-point dimensions.
    Non-numeric dimensions (should raise a TypeError, similar to Exercise 2 above).


"""

import pytest
from rectangle import calculate_rectangle_area


def test_calculate_rectangle_area_positive():
    assert calculate_rectangle_area(5, 4) == 20


def test_calculate_rectangle_area_zero():
    assert calculate_rectangle_area(0, 10) == 0


def test_calculate_rectangle_area_negative():
    with pytest.raises(ValueError):
        calculate_rectangle_area(-5, 4)  # Expect a ValueError to be raised


def test_calculate_rectangle_area_floating_numbers():
    assert calculate_rectangle_area(5.5, 4.4) == pytest.approx(24.2)


def test_calculate_rectangle_area_non_numeric():
    with pytest.raises(TypeError):
        calculate_rectangle_area("test", 1)
    with pytest.raises(TypeError):
        calculate_rectangle_area(1, "test")
    with pytest.raises(TypeError):
        calculate_rectangle_area("test", "test")
