import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Test for 'city_functions'"""

    def test_city(self):
        """Do names like 'Santiago, Chile' work"""
        formatted_city = city_country('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_population(self):
        """Do names like 'Santiago, Chile - Population 500000 work'"""
        formatted_city = city_country('santiago', 'chile', 500000)
        self.assertEqual(
            formatted_city, 'Santiago, Chile - Population 500000')


if __name__ == '__main__':
    unittest.main()
