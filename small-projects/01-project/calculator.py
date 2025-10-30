# calculator.py

# calculator.py
from typing import Union


def check_input(a: Union[int, float], b: Union[int, float]) -> None:
    """
    Validates if both inputs are numeric (int or float).
    Raises:
        TypeError: If either input is not a number.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numeric.")


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers and returns the sum.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The sum of a and b.
    """
    check_input(a, b)
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtracts the second number from the first and returns the difference.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The difference between a and b.
    """
    check_input(a, b)
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiplies two numbers and returns the product.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The product of a and b.
    """
    check_input(a, b)
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divides the first number by the second and returns the quotient.
    Raises:
        ZeroDivisionError: If the second number (b) is zero.
        TypeError: If either input is not a number.
    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.
    Returns:
        int or float: The quotient of a and b.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    check_input(a, b)
    return a / b


def power(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Raises the first number to the power of the second and returns the result.
    Args:
        a (int or float): The base number.
        b (int or float): The exponent.
    Returns:
        int or float: The result of a raised to the power of b.
    """
    check_input(a, b)
    return a**b


# Example usage (for manual testing, but we'll focus on automated tests):
if __name__ == "__main__":
    print(f"5 + 3 = {add(3, 5)}")  # Expected: 8
    print(f"10 - 4 = {subtract(10, 4)}")  # Expected: 6
    print(f"7 * 2 = {multiply(7, 2)}")  # Expected: 14
    print(f"15 / 3 = {divide(15, 3)}")  # Expected: 5
    # print(f"11 / 0 = {divide(10, 0)}")  # This would raise an error
    print(f"2^3 = {power(2, 3)}")
    # To demonstrate TypeError in __main__:
    # try:
    #     add(1, 'a')
    # except TypeError as e:
    #     print(f"Caught expected error: {e}")
