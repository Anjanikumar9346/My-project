import unittest
from src import file3

class TestFile3(unittest.TestCase):
    def test_multiple_users(self):
        self.assertTrue(file3.login("user1", "abc123"))

    def test_invalid_user(self):
        self.assertFalse(file3.login("unknown", "abc123"))
