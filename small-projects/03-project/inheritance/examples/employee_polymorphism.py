class Employee:
    def __init__(self, name, employee_id):
        (self.name,) = (name,)
        self.employee_id = employee_id

    def display_details(self):
        print(f"Name: {self.name}, Employee ID: {self.employee_id}")


class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def display_details(self):
        # Overriding the method
        print(
            f"Developer: {self.name}, ID: {self.employee_id}, Lang: {self.programming_language}"
        )


class Manager(Employee):
    def __init__(self, name, employee_id, team_size):
        super().__init__(name, employee_id)
        self.team_size = team_size

    def display_details(self):
        # Overriding the method
        print(
            f"Manager: {self.name}, ID: {self.employee_id}, Team Size: {self.team_size}"
        )


# Demonstrating Polymorphism
employees = [
    Employee("Grace Hopper", "EMP100"),
    Developer("Alan Turing", "EMP101", "Python"),
    Manager("Ada Lovelace", "EMP102", 5),
]

for emp in employees:
    emp.display_details()
