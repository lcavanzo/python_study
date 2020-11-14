"""class to model a Employee"""

class Employee:
    """A simple attempt to represent a employee"""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the Employee attributes"""
        self.first_name = first_name
        self.last_name  = last_name
        self.annual_salary = annual_salary

    def __repr__(self):
        """Show info about the employee"""
        return f"{self.first_name} {self.last_name} {self,annual_salary}"

    def give_raise(self, raise_mount=5000):
        """Give a raise to the employee, 5000 by default"""
        self.annual_salary += raise_mount
