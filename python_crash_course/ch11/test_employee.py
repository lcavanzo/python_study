import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""
    
    def setUp(self):
        """
        Create a employee, set information for use in all test methods
        """
        self.e1 = Employee('luis', 'cavanzo', 10000)
        
    def test_give_default(self):
        """Test that test default raise is working properly"""
        self.e1.give_raise()
        self.assertEqual(self.e1.annual_salary, 15000)

    def test_give_custom_raise(self):
        """Test that test custom raise is working properly"""
        self.e1.give_raise(10000)
        self.assertEqual(self.e1.annual_salary, 20000)


if __name__ == '__main__':
    unittest.main()
