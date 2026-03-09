class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute(name mangled)

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print(f"Salary updated to: {self.__salary}")
        else:
            print("Salary must be positive.")

    def __calculate_tax(self):  # Private method(name mangled)
        return self.__salary * 0.10

    def get_net_salary(self):
        tax = self.__calculate_tax()
        return self.__salary - tax


# Demonstration
e = Employee("Charlie", 60000)
print(f"Employee Name: {e.name}")
print(f"Gross Salary: {e.get_net_salary()}")
print(f"Net Salary: {e.get_salary()}")

# Attempting direct access to private attribute (will raise AttributeError)
try:
    print(e.__salary)
except AttributeError as ex:
    print(f"Arror trying to access __salary directly: {ex}")

# Accessing via name mangling (possible, but strongly discouraged and defeats purpose)
print(f"Accessing via name mangling: {e._Employee__salary}")
e._Employee__salary = 70000  # Direct modification via mangled name

print(f"Gross Salary after mangled modification: {e.get_salary()}")

# Attempting direct access to private method (will raise AttributeError)
try:
    e.__calculate_tax()
except AttributeError as ex:
    print(f"Error trying to call __calculate_tax direclty: {ex}")
    A
