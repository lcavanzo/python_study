"""
Area Calculator:

    Task: Create a new Python file (e.g., geometry.py) and define a function calculate_rectangle_area(length, width) that returns the area of a rectangle.
"""


def validate_input(a, b):
    if not (isinstance(a, (int, float)) and (isinstance(b, (int, float)))):
        raise TypeError("Numeric value is needed.")


def calculate_rectangle_area(length, width):
    validate_input(length, width)
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative.")
    return length * width


if __name__ == "__main__":
    print(validate_input("test", 1))
    print(validate_input(1, "test"))
    print(validate_input("tes1", "test"))
