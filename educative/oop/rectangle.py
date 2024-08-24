#! python 3

# rectangle.

"""
Problem statement
You are given a partially completed code of a Rectangle class in the editor. Implement the class by completing the tasks below.

Task 1
Implement a constructor to initialize the values of two private properties: length and width.

Task 2
Implement a method, area(), in the Rectangle class that returns the product of length and width. See the formula below:

Area=length×width

Sample properties

length = 4
width = 5

Sample method output
20

Task 3
Implement a method, perimeter(), in the Rectangle class that returns two times the sum of length and width. See the formula below:

Perimeter=2×(length+width)

Sample properties

length = 4
width = 5
Sample method output

18
"""


class Rectangle:
    """docstring for Rectangle."""

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


r = Rectangle(4, 5)
print(f"Area = {r.area()}")
print(f"Perimeter= {r.perimeter()}")
