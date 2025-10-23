"""
Factorial Calculation: Write a function that calculates the factorial of a non-negative
integer.
Test it with 0, 1, and a larger number like 10. How should it handle negative inputs?
Add a test to check this.
"""


def factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif number == 0:
        return 1  # Factorial of 0 is 1
    else:
        fact = 1
        for n in range(1, number + 1):
            fact *= n
        return fact


# Test cases
print(f"Factorial of 0 -> {factorial(0)}")
print(f"Factorial of 3 -> {factorial(3)}")
print(f"Factorial of 10 -> {factorial(10)}")


# Test with assert and try-except
assert factorial(0) == 1
assert factorial(3) == 6
assert factorial(10) == 3628800

try:
    factorial(-2)
except ValueError as e:
    print(f"Caught expected error: {e}")
    assert True  # Test that the ValueError was raised
else:
    assert False, "ValueError was not raised for negative input"  # Fail if no error

print("All test cases passed!")
