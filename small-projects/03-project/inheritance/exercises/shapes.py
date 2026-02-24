"""
Objective: Create a class hierarchy for geometric shapes and test their area calculation.

    Create a base class Shape:
        Initialize with a name attribute.
        Define a method area() that raises a NotImplementedError (this indicates that subclasses must implement their own area calculation).
        Define a method get_description() that returns a string like "This is a generic Shape."

    Create a subclass Circle:
        Inherit from Shape.
        Initialize with name and radius. Call the parent constructor.
        Implement the area() method to calculate the circle's area (π * radius²). Use math.pi.
        Override get_description() to return "This is a Circle with radius X."

    Create a subclass Rectangle:
        Inherit from Shape.
        Initialize with name, width, and height. Call the parent constructor.
        Implement the area() method to calculate the rectangle's area (width * height).
        Override get_description() to return "This is a Rectangle with width X and height Y."

    Polymorphism Testing:
        Using the unittest framework, write a test class TestShapes.
        Test that calling area() on an instance of Shape correctly raises NotImplementedError.
        Test the area() method for Circle with a known radius, asserting the calculated area.
        Test the area() method for Rectangle with known dimensions, asserting the calculated area.
        Create a list containing instances of Circle and Rectangle. Iterate through the list, call area() on each, and assert that the correct area is returned based on the object's type.
        Test the get_description() method for each shape type.
"""

from abc import ABC, abstractmethod
import math
import unittest


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        """Mandatory method for all the shapes"""
        raise NotImplementedError

    def get_description(self) -> str:
        """
        Return Shape description
        """
        return "This is a generic Shape."


class Circle(Shape):
    """
    Class that represents a Circle
    """

    def __init__(self, name, radius):
        """
        Initialize Circle class
        """

        super().__init__(name)
        self.radius = radius

    def area(self):
        """
        Overriding Area method for a circle shape
        """

        return math.pi * (self.radius**2)

    def get_description(self) -> str:
        """
        Shows Circle description
        """
        return f"This is Circle with radius {self.radius}."


class Rectangle(Shape):
    """
    Class that represents a Rectangle
    """

    def __init__(self, name, width, height):
        """
        Initialize Rectangle class
        """

        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        """
        Overriding Area method for a rectangle shape
        """

        return self.width * self.height

    def get_description(self) -> str:
        """
        Shows Rectangle description
        """
        return f"This is Rectangle with {self.width} width and {self.height} height."


# shape1 = Shape("Shape")
# # print(shape1.area())
# print(shape1.get_description())
#
# c1 = Circle("c1", 10)
# print(c1.get_description())
# print(c1.area())
#
# r1 = Rectangle("r1", 10, 5)
# print(r1.get_description())
# print(r1.area())


class TestShapes(unittest.TestCase):
    """
    Tests for testing the behiviour of different shapes
    """

    def test_shape_area_ok(self):
        # Test the base class behavior

        sh = Shape("sh01")
        self.assertRaises(NotImplementedError, sh.area)

    def test_circle_area_ok(self):
        # Test the Circle area method

        c1 = Circle("c1", 10)
        area = c1.area()
        # This allows the value to be off by 0.0001
        self.assertAlmostEqual(area, 314.15926, delta=0.0001)

    def test_rectangle_area_ok(self):
        # Test the Rectangle area method

        r1 = Rectangle("r1", 5, 10)
        area = r1.area()
        self.assertEqual(area, 50)

    def test_get_description_polyphormic_list_iterations(self):
        # Test the get_description Polymorphism
        shapes = [Shape("sh1"), Circle("c1", 10), Rectangle("r1", 5, 10)]
        expected_outputs = [
            "This is a generic Shape.",
            "This is Circle with radius 10.",
            "This is Rectangle with 5 width and 10 height.",
        ]
        for index, shape in enumerate(shapes):
            self.assertEqual(shape.get_description(), expected_outputs[index])

    def test_area_polyphormic_list_iterations(self):
        # Test the area Polymorphism
        shapes = [Shape("sh1"), Circle("c1", 10), Rectangle("r1", 5, 10)]
        expected_outputs = [
            "NotImplementedError",
            314.159265,
            50,
        ]
        for index, shape in enumerate(shapes):
            try:
                self.assertAlmostEqual(
                    shape.area(), expected_outputs[index], delta=0.0001
                )
            except NotImplementedError:
                self.assertEqual("NotImplementedError", expected_outputs[index])


if __name__ == "__main__":
    unittest.main()
