# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide, power, check_input


@pytest.fixture
def sample_numbers():
    return (10, 5)


def test_add_with_fixtures(sample_numbers):
    num1, num2 = sample_numbers
    assert add(num1, num2) == 15


def test_add_positive_numbers():
    """Test addition with two positive numbers."""
    assert add(5, 3) == 8


def test_add_negative_numbers():
    """Test addition with two negative numbers."""
    assert add(-5, -3) == -8


def test_add_positive_and_negative_numbers():
    """Test addition with a positive and a negative number."""
    assert add(10, -4) == 6


def test_add_zero():
    """Test addition with zero."""
    assert add(7, 0) == 7
    assert add(0, 7) == 7
    assert add(0, 0) == 0


def test_subtract_positive_numbers(sample_numbers):
    """Test subtraction with positive numbers."""
    # assert subtract(10, 4) == 6
    num1, num2 = sample_numbers
    assert subtract(num1, num2) == 5


def test_subtract_negative_numbers():
    """Test subtraction with negative numbers."""
    assert subtract(-5, -3) == -2


def test_subtract_result_is_negative():
    """Test subtraction where the result is negative."""
    assert subtract(3, 8) == -5


def test_multiply_positive_numbers():
    """Test multiplication with two positive numbers."""
    assert multiply(5, 3) == 15


def test_multiply_negative_numbers():
    """Test multiplication with two negative numbers."""
    assert multiply(-5, -3) == 15


def test_multiply_positive_and_negative_numbers():
    """Test multiplication with a positive and a negative number."""
    assert multiply(10, -2) == -20


def test_multiply_by_zero():
    """Test multiplication by zero."""
    assert multiply(7, 0) == 0
    assert multiply(0, 7) == 0
    assert multiply(0, 0) == 0


def test_divide_positive_numbers():
    """Test division with two positive numbers."""
    assert divide(15, 3) == 5


def test_divide_negative_numbers():
    """Test division with two negative numbers."""
    assert divide(-10, -2) == 5


def test_divide_positive_by_negative():
    """Test division with a positive numerator and negative denominator."""
    assert divide(10, -2) == -5


def test_divide_by_one():
    """Test division by one."""
    assert divide(10, 1) == 10


def test_divide_zero_by_number():
    """Test division of zero by a non-zero number."""
    assert divide(0, 5) == 0


def test_divide_by_zero():
    """Test that ZeroDivisionError is raised when dividing by zero."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        divide(10, 0)


def test_divide_floating_point_numbers():
    """Test division with floating point numbers, considering precision."""
    assert divide(10.0, 3.0) == pytest.approx(3.333333)  # Use pytest.approx for floats


def test_power_positive_numbers():
    """Test power with positive int numbers"""
    assert power(2, 3) == 8


def test_power_negative_numbers():
    """Test power with negative int numbers"""
    assert power(-2, 3) == -8


def test_power_by_zero():
    """Test power by zero"""
    assert power(2, 0) == 1


def test_add_non_numeric_input():
    with pytest.raises(TypeError, match="Inputs must be numeric."):
        add(1, "b")
    with pytest.raises(TypeError, match="Inputs must be numeric."):
        add("a", 2)
