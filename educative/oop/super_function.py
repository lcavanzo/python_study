"""
Problem statement
When a method in a derived class overrides a method in a base class, it is still possible to call
the overridden method using the super() function.

If you write super().method(), it will call the method that was defined in the superclass.

You are given a partially completed code in the editor.
Modify the code so that it returns the following:

Sample input
circle = XShape("Circle");
circle.getName()

Sample output
"Shape, Circle"
The Shape class is already prepended in the code and it has one property,
sname and one method, getName(). getName() returns sname.
"""


class Shape:
    """docstring for Shape."""

    sname = "Shape"

    def getName(self):
        return self.sname


class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return f"{super().getName()}, {self.xsname}"


circle = XShape("Circle")
print(circle.getName())
