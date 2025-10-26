"""
Error Handling: Write a function called divide that takes two numbers, numerator and denominator, as input.
If the denominator is zero, the function should raise a ValueError with the message "Cannot divide by zero".
Otherwise, it should return the result of the division.

Write pytest tests to ensure that the function raises the ValueError when the denominator is zero and returns the correct result otherwise.
"""


def divide(numerator: int, denominator: int) -> float:
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return numerator / denominator


# print(divide(2, 5))
# print(divide(10, 1))
# print(divide(0, 10))
# print(divide(2, 0))
