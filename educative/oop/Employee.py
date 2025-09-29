class Employee:
    def __init__(self, ID=None, salary=None, department=None) -> None:
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self, title=None):
        return self.salary * 0.2

    def salaryPerDay(self):
        return self.salary / 30

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)


Steve = Employee(1000, 2500, "ID")
#
Steve.title = "Manager"

print(Steve.ID)
print(Steve.salary)
print(Steve.department)
print(Steve.title)

print(Steve.tax())
print(Steve.salaryPerDay())

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)
