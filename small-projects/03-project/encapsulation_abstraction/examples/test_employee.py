import pytest
import hashlib


# Re-define the Employee class for clarity in testing context
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            return True
        else:
            print("Salary must be positive.")
            return False

    def __calculate_tax(self):  # Private method(name mangled)
        return self.__salary * 0.10

    def get_net_salary(self):
        tax = self.__calculate_tax()
        return self.__salary - tax


# Test employee
def test_employee_initialization():
    employee = Employee("Alice", 50000)
    assert employee.name == "Alice"
    # Cannot directly access __salary, so we check through get_salary
    assert employee.get_salary() == 50000


def test_get_salary():
    employee = Employee("Bob", 60000)
    assert employee.get_salary() == 60000


def test_set_salary_valid():

    employee = Employee("Charlie", 70000)
    assert employee.set_salary(75000) is True
    assert employee.get_salary() == 75000


def test_set_salary_invalid():
    employee = Employee("David", 80000)
    assert employee.set_salary(-1000) is False
    assert employee.get_salary() == 80000  # Salary should remaing unchanged


def test_get_net_salary():
    employee = Employee("Eve", 100000)
    # Expected net salary: 100000 - (100000 * 0.10) = 90000
    assert employee.get_net_salary() == 90000.0


def test_private_attribute_access_via_name_mangling():
    employee = Employee("Frank", 90000)
    # This test demonstrate that it's *posible* to access the mangled name,
    # but it's not recommended practice for external code.
    # It confirms Python's __ mechanims is name mangling, not true privacy
    # 1. We construct the secret handshake string: "_Employee__salary"
    mangled_salary_attr = f"_{Employee.__name__}__salary"
    assert hasattr(employee, mangled_salary_attr)
    # 2. We use 'getattr' to bypass the locked door and grab the money!
    assert getattr(employee, mangled_salary_attr) == 90000

    # Test modification via mangled name(again, to show it's posible)
    setattr(employee, mangled_salary_attr, 95000)
    assert employee.get_salary() == 95000


def test_private_method_access_via_name_mangling():
    employee = Employee("Grace", 120000)
    # Similar to attributes, private methods are also name mangled
    mangled_calc_tax_method = f"_{Employee.__name__}__calculate_tax"
    assert hasattr(employee, mangled_calc_tax_method)

    # You can call it using getattr, but it's against encapsulation
    calc_tax_func = getattr(employee, mangled_calc_tax_method)
    assert calc_tax_func() == 120000 * 0.10


def test_no_direct_private_attribute_access():
    employee = Employee("Heidi", 50000)
    # Assert that trying to access __salary direclty raises AttributeError
    with pytest.raises(AttributeError):
        employee.__salary


def test_no_direct_private_method_access():
    employee = Employee("Ivan", 50000)
    # Assert that trying to call __calculate_tax directly raises AttributeError
    with pytest.raises(AttributeError):
        employee.__calculate_tax()


if __name__ == "__main__":
    pytest.main()
