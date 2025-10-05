class Circle:
    # Insert your code here
    def __init__(self, radius):
        self.radius = radius

    def print_area(self):
        PI = 3.14
        print(f" {PI * (self.radius * self.radius)}")


obj = Circle(3)
obj.print_area()
