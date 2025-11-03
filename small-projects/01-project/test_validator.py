# test_validator.py
import pytest
from validator import divide, validate_age


def test_divide_by_zero_raises_value_error():
    """Verify that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)


def test_divide_by_zero_raises_value_error_with_message():
    """Verify specific error message when dividing by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_validate_age_non_int_raises_type_error():
    """Verify non-integer age raises TypeError."""
    with pytest.raises(TypeError, match="Age must be an integer"):
        validate_age("twenty")


def test_validate_age_negative_raises_value_error():
    """Verify negative age raises ValueError."""
    with pytest.raises(ValueError, match="Age cannot be negative"):
        validate_age(-5)
