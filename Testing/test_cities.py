import unittest
from Testing.city_functions import cityString

class cityTests(unittest.TestCase):

    def test_city_function(self):
        result = cityString("london", "England")
        self.assertEqual(result, "london, England")