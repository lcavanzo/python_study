# test_divide.py

import pytest
from divide import divide


def test_divide_normal():
    assert divide(10, 2) == 5


def test_divide_denominator_zero():
    with pytest.raises(ValueError):
        divide(2, 0)
