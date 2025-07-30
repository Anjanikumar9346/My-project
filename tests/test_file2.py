import unittest
from src import file2

class TestFile2(unittest.TestCase):
    def test_case_insensitive(self):
        self.assertTrue(file2.login("ADMIN", "password123"))

    def test_invalid_password(self):
        self.assertFalse(file2.login("admin", "1234"))
