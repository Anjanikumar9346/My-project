import unittest
from src import file4

class TestFile4(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(file4.login("admin", "password123"))

    def test_short_password(self):
        self.assertFalse(file4.login("admin", "123"))
