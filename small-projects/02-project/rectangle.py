# rectangle
def calculate_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non negative")
    return length * width
