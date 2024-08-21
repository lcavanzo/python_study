"""
Problem statement
You have to implement a Sedan class, which inherits from the Car class and contains a SedanEngine object.

Note: In such a composition relation, the Sedan class will be responsible for SedanEngine lifetime.

Consider this diagram for reference:



Task 1
The Car initializer should take arguments in the order Car(model,color).

The Car class should have two properties:

model
color
The Car class should have one method:

printDetails(), which will print model and color of the Car object
Task 2
The SedanEngine class will have two methods:
start(), which will print:
Car has started.
stop(), which will print:
Car has stopped.
Task 3
The Sedan initializer should take arguments in the order Sedan(model, color).

The Sedan class will have one property:

engine, which is a SedanEngine class object that should be created when the object is initialized
The Sedan class will have two methods:

setStart(), which will call the start() method of SedanEngine.

setStop(), which will call the stop() method of SedanEngine.

Sample input
car1 = Sedan("Toyota","Grey")
car1.setStart()
car1.printDetails()
car1.setStop()
Sample output
After the implementation of your classes, the code below should produce the following output:

Car has started.
Model: Toyota
Color: Grey
Car has stopped.
"""


class Car:
    """docstring for Car."""

    def __init__(self, model="", color=""):
        self.model = model
        self.color = color

    def printDetails(self):
        """docstring for Car class"""
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")


class SedanEngine:
    """docstring for SedanEngine."""

    def start(self):
        print("Car has started")

    def stop(self):
        print("Car has stopped")


class Sedan(Car):
    """docstring for Sedan."""

    def __init__(self, model, color):
        super().__init__(model, color)
        self.engine = SedanEngine()

    def setStart(self):
        self.engine.start()

    def setStop(self):
        self.engine.stop()


car1 = Sedan("Toyota", "Grey")
car1.setStart()
car1.printDetails()
car1.setStop()
