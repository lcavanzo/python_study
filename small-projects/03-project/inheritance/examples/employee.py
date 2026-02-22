class Employee:
    def __init__(self, name, employee_id):
        (self.name,) = (name,)
        self.employee_id = employee_id

    def display_details(self):
        """
        Display the basic details fo an employee.
        """
        print(f"Name: {self.name}, Employee ID: {self.employee_id}")


class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        # Call the parent class's __init__ method to initialize inherited attributes
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def display_details(self):
        """
        Overrides the parte's display_details to include programming language
        """
        super().display_details()  # Call the parent's display_details
        print(f"Role: Developer, Language:{self.programming_language}")


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def display_details(self):
        """
        Overrides the parent's display_details to include team size.
        """
        super().display_details()
        print(f"Role: Manager, Team Size: {self.team_size}")


# Example usage of the Empleyee class
general_employee = Employee("Alice Smith", "EMP0001")
general_employee.display_details()

print("-" * 20)

# Example usage of child classes
dev1 = Developer("Bob Johnson", "EMP002", "Python")
dev1.display_details()

print("-" * 20)

mgr1 = Manager("Carol White", "EMP003", 5)
mgr1.display_details()
