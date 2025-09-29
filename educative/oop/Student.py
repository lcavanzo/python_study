class Student:
    __name = None
    __rollNumber = None

    def getName(self):
        return self.__name

    def setName(self, name=None):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber=None):
        self.__rollNumber = rollNumber


obj = Student()
obj.setName("cavanzo")
obj.setRollNumber(101)

print(obj.getName())
print(obj.getRollNumber())
