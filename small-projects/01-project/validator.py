# validator.py
def divide(a, b):
    """Divides two numbers. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def validate_age(age):
    """Raises TypeError if age is not an int, ValueError if age is negative."""
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return True
