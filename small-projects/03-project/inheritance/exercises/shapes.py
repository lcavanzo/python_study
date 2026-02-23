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

import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        """Mandatory method for all the shapes"""
        raise NotImplementedError

    def get_description(self):
        """
        Return Shape description
        """
        return "This is a generic Shape."


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def get_description(self):
        """
        Shows Circle description
        """
        return f"This is Circle with radius {self.radius}."
