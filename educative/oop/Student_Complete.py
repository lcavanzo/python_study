#! python3

# Student_Complete.py

"""
Problem statement#
Implement the complete Student class by completing the tasks below

Task
Implement the following properties as private:

name
rollNumber
Include the following methods to get and set the private properties above:

getName()
setName()
getRollNumber()
setRollNumber()
Implement this class according to the rules of encapsulation.

Input
Checking all the properties and methods

Output
Expecting perfectly defined fields and getter/setters

Note: Do not use initializers to initialize the properties. Use the set methods to do so. If the setter is not defined properly, the corresponding getter will also generate an error even if the getter is defined properly.
"""


class Student:
    """docstring for Student."""

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
