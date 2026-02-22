class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"This is a {self.color} shape."


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def describe(self):
        # Call parent's describe method and extend it
        parent_description = super().describe()
        return f"{parent_description} It is a circle with radius {self.radius}"


# Example of super()
my_cyrcle = Circle("blue", 10)
print(my_cyrcle.describe())
