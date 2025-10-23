# test_rectangle.py
import pytest
from rectangle import calculate_area


def test_calculate_area_positive():
    assert calculate_area(5, 4) == 20


def test_calculate_area_zero():
    assert calculate_area(0, 10) == 0


def test_calculate_area_negative():
    with pytest.raises(ValueError):
        calculate_area(-5, 4)  # Expect a ValueError to be raised
