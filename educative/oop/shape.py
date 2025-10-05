class Shape:
    def __init__(self):
        self.sname = "Shape"

    def getName(self):
        return self.sname


class XShape(Shape):
    def __init__(self, name):
        # we call init without argument becase the parent class doesn't ask for it
        super().__init__()
        self.xsname = name

    def getName(self):
        return super().getName() + ", " + self.xsname


# t1 = Shape()
# print(t1.getName())

circle = XShape("Circle")
print(circle.getName())
