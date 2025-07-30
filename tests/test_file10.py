import unittest
from src import file10

class TestFile10(unittest.TestCase):
    def test_valid_special_char(self):
        self.assertTrue(file10.login("admin", "pa$$word123"))

    def test_missing_special_char(self):
        self.assertFalse(file10.login("admin", "password123"))
