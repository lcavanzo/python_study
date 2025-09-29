class Rectangle:
    def __init__(self, length, width) -> None:
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


obj = Rectangle(4, 5)
print(obj.area())

print(obj.perimeter())
