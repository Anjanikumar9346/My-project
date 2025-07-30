import unittest
from src import file9

class TestFile9(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(file9.login("admin@example.com", "password123"))

    def test_invalid_email_format(self):
        self.assertFalse(file9.login("adminexample.com", "password123"))
