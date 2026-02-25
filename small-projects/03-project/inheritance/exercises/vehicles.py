"""
Vehicle Management (Polymorphism in Action)

Objective: Model different vehicles and demonstrate polymorphic behavior in a transportation system.

    Create a base class Vehicle:
        Initialize with make and model.
        Define a method start_engine() that prints "The [make] [model] engine starts."
        Define a method drive() that prints "The [make] [model] is driving."

    Create a subclass Car:
        Inherit from Vehicle.
        Initialize with make, model, and num_doors.
        Override drive() to print "The [make] [model] with [num_doors] doors is cruising."

    Create a subclass Motorcycle:
        Inherit from Vehicle.
        Initialize with make, model, and has_sidecar (boolean).
        Override drive() to print "The [make] [model] is roaring down the road." (If has_sidecar is True, append " with a sidecar!")

    Polymorphism Testing:
        Using the unittest framework, create a test class TestVehicles.
        Test that Vehicle's start_engine() and drive() methods work as expected.
        Test that Car's overridden drive() method produces the correct output, including num_doors.
        Test that Motorcycle's overridden drive() method produces the correct output, distinguishing between has_sidecar being true or false.
        Create a list of Vehicle objects, including instances of Car and Motorcycle.
        Iterate through this list, call start_engine() on each, and then drive() on each. Assert that the printed output (you might need to capture stdout or modify drive() to return a string for easier testing) correctly reflects the specific type of vehicle and its overridden behavior.

"""

import unittest


class Vehicle:
    """
    Base class that represents a Vehicle
    """

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"Vehicle(make='{self.make}', model='{self.model}')"

    def start_engine(self):
        """
        method that represents the start engine
        """

        return f"The {self.make} {self.model} engine starts."

    def drive(self):
        """
        method that represents the a car driving
        """
        return f"The {self.make} {self.model} is driving."


class Car(Vehicle):
    """
    Class that represents a Car
    """

    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', num_doors='{self.num_doors}')"

    def drive(self):
        """
        methond that represents the driving for a car
        """
        return f"The {self.make} {self.model} with {self.num_doors} doors is cruising."


class Motorcycle(Vehicle):
    """
    Class that represents a Motorcycle
    """

    def __init__(self, make, model, has_sidecar: bool):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar

    def __repr__(self):
        return f"Motorcycle(make='{self.make}', model='{self.model}', has_sidecar='{self.has_sidecar}')"

    def drive(self):
        """
        method that represents the driving for Motorcycle
        """
        if self.has_sidecar:
            return (
                f"The {self.make} {self.model} is roaring down the road with a sidecar!"
            )
        else:
            return f"The {self.make} {self.model} is roaring down the road."


class TestVehicles(unittest.TestCase):
    """
    Class for testing all the vehicles behavior for drive method
    """

    def test_vehicle_drive_ok(self):
        """
        testing the correct behavior of the base class
        """
        vh1 = Vehicle("Tesla", "Y")

        expected_msg = "The Tesla Y is driving."
        self.assertEqual(vh1.drive(), expected_msg)

    def test_vehicle_start_engine_ok(self):
        """
        testing the correct behavior of the base class for start_engine method
        """
        vh1 = Vehicle("Tesla", "Y")

        expected_msg = "The Tesla Y engine starts."
        self.assertEqual(vh1.start_engine(), expected_msg)

    def test_car_drive_ok(self):
        """
        testing the correct behavior of the child Car class for drive method
        """

        car1 = Car("BYD", "Dolphin", 4)

        expected_msg = "The BYD Dolphin with 4 doors is cruising."
        self.assertEqual(car1.drive(), expected_msg)

    def test_motorcycle_drive_true_ok(self):
        """
        testing the correct behavior of the child Motorcycle class for drive method
        """

        mt1 = Motorcycle("Chopper", "Strip", True)

        expected_msg = "The Chopper Strip is roaring down the road with a sidecar!"
        self.assertEqual(mt1.drive(), expected_msg)

    def test_motorcycle_drive_false_ok(self):
        """
        testing the correct behavior of the child Motorcycle class for drive method
        """

        mt1 = Motorcycle("Chopper", "Strip", False)

        expected_msg = "The Chopper Strip is roaring down the road."
        self.assertEqual(mt1.drive(), expected_msg)

    def test_list_vehicles_drive_polymorphims(self):
        """
        Test the Polymorphism for each class for drive method
        """
        vehicles = [
            Vehicle("Tesla", "Y"),
            Car("BYD", "Dolphin", 4),
            Motorcycle("Chopper", "Strip", True),
            Motorcycle("Chopper", "Strip", False),
        ]
        expected_outputs = [
            "The Tesla Y is driving.",
            "The BYD Dolphin with 4 doors is cruising.",
            "The Chopper Strip is roaring down the road with a sidecar!",
            "The Chopper Strip is roaring down the road.",
        ]
        # for index, vehicle in enumerate(vehicles):
        #     self.assertEqual(vehicle.drive(), expected_outputs[index])
        for vehicle, expected_output in zip(vehicles, expected_outputs):
            self.assertEqual(vehicle.drive(), expected_output)

    def test_list_vehicles_start_engine_polymorphims(self):
        """
        Test the Polymorphism for each class for the start engine method
        """
        vehicles = [
            Vehicle("Tesla", "Y"),
            Car("BYD", "Dolphin", 4),
            Motorcycle("Chopper", "Strip", True),
            Motorcycle("Chopper", "Strip", False),
        ]
        expected_outputs = [
            "The Tesla Y engine starts.",
            "The BYD Dolphin engine starts.",
            "The Chopper Strip engine starts.",
            "The Chopper Strip engine starts.",
        ]

        for vehicle, expected_output in zip(vehicles, expected_outputs):
            self.assertEqual(vehicle.start_engine(), expected_output)

    def test_all_clases_correct_instance(self):
        """
        Test the Polymorphism for each class
        """
        classes = [Vehicle, Car, Motorcycle, Motorcycle]
        vehicles = [
            Vehicle("Tesla", "Y"),
            Car("BYD", "Dolphin", 4),
            Motorcycle("Chopper", "Strip", True),
            Motorcycle("Chopper", "Strip", False),
        ]
        for vehicle, cl in zip(vehicles, classes):
            self.assertIsInstance(vehicle, cl)


if __name__ == "__main__":
    unittest.main()
