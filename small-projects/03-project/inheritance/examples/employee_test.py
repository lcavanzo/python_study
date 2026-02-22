import unittest
from unittest.mock import ThreadingMock


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def get_details_strings(self):
        """
        Returns a string with basic employee details
        """
        return f"Name: {self.name}, Employee ID: {self.employee_id}"


class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def get_details_strings(self):
        """
        Retuns a string with developer details, overriding the parent
        """
        return f"Developer: {self.name}, ID: {self.employee_id}, Lang: {self.programming_language}"


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def get_details_strings(self):
        """
        Returns a string with manager details, overriding the parent
        """
        return (
            f"Manager: {self.name}, ID: {self.employee_id}, Team Size: {self.team_size}"
        )


class TestEmployeePolymorphism(unittest.TestCase):
    def test_employee_details(self):
        # Test the base class behavior
        employee = Employee("Alice", "E100")
        self.assertEqual(
            employee.get_details_strings(),
            "Name: Alice, Employee ID: E100",
        )

    def test_developer_details_polymorphism(self):
        # Test the overriden behavior in Developer child class
        developer = Developer("Bob", "D200", "Python")
        self.assertEqual(
            developer.get_details_strings(), "Developer: Bob, ID: D200, Lang: Python"
        )

    def test_manager_details_polymorphism(self):
        # Test the overriden behavior in Manager child class
        manager = Manager("Charlie", "M300", 10)
        self.assertEqual(
            manager.get_details_strings(), "Manager: Charlie, ID: M300, Team Size: 10"
        )

    def test_polymorphic_list_iteratios(self):
        # Test how a mixed list of objects behaves with polymorphic method call
        employees = [
            Employee("Dave", "E400"),
            Developer("Eve", "D500", "Java"),
            Manager("Frank", "M600", 3),
        ]

        expected_outputs = [
            "Name: Dave, Employee ID: E400",
            "Developer: Eve, ID: D500, Lang: Java",
            "Manager: Frank, ID: M600, Team Size: 3",
        ]

        for i, emp in enumerate(employees):
            # Assert that correct string is returned for each object type
            self.assertEqual(emp.get_details_strings(), expected_outputs[i])


# To run these tests, you would typically save this in a file (e.g., test_employees.py)
# and run `python -m unittest test_employees.py` from your terminal.
# Or, if you prefer, you can add this block to run it directly:
if __name__ == "__main__":
    unittest.main()
