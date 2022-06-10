class Employee:
    """Try to model a employee"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def give_raise(self, new_raise=5000):
        """Add the new raise to the annual salary"""
        self.annual_salary += int(new_raise)

    def show_employee(self):
        """Show employee's information"""
        name = f"{self.first_name} {self.last_name}"
        print(f"{name} - {self.annual_salary}")

#e1 = Employee('luis', 'cavanzo', '10000')
#e1.show_employee()
#e1.give_raise()
#e1.show_employee()
#e1.give_raise(1000)
#e1.show_employee()
#

