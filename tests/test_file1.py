import unittest
from src import file1

class TestFile1(unittest.TestCase):
    def test_valid_login(self):
        self.assertTrue(file1.login("admin", "password123"))

    def test_invalid_login(self):
        self.assertFalse(file1.login("admin", "wrongpass"))
