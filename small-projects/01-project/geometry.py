# geometry.py
import math


def calculate_circle_area(radius):
    """Calculates the area of a circle given its radius."""
    return math.pi * (radius**2)


# test_geometry.py
import pytest
from geometry import calculate_circle_area


def test_circle_area_with_radius_1():
    """Test circle area for radius 1."""
    # Expected area is pi * 1^2 = pi = 3.1415926535...
    assert calculate_circle_area(1) == pytest.approx(3.14159)


def test_circle_area_with_radius_2():
    """Test circle area for radius 2."""
    # Expected area is pi * 2^2 = 4pi = 12.56637...
    assert calculate_circle_area(2) == pytest.approx(12.566)
