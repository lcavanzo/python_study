import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test for the Employee class"""

    def setUp(self):
        """Create a employee """
        self.my_employee1 = Employee('luis', 'cavanzo', 10000)

    def test_give_default_raise(self):
        """Test a single raise of 5000"""
        self.my_employee1.give_raise()
        self.assertEqual(self.my_employee1.annual_salary, 15000)

    def test_give_custom_raise(self):
        """Test a custom raise to the annual salary"""
        self.my_employee1.give_raise(10000)
        self.assertEqual(self.my_employee1.annual_salary, 20000)
        


if __name__ == '__main__':
    unittest.main()
