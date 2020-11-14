import unittest
from cities_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Test for 'cities_funtions.py'"""

    def test_city_country(self):
        """Do info like 'Santiago Chile' works"""
        formatted_city_info = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city_info, 'Santiago, Chile')
        formatted_city_info = get_formatted_city('veracruz', 'mexico')
        self.assertEqual(formatted_city_info, 'Veracruz, Mexico')

    def test_city_country_population(self):
        """Do info like 'Santiago, Chile - 5000000' works?"""
        formatted_city_info = get_formatted_city('santiago', 'chile',
                '5000000')
        self.assertEqual(formatted_city_info, 'Santiago, Chile'
                f' - population 5000000')
        


if __name__ == '__main__':
    unittest.main()
