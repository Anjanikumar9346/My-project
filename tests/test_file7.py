import unittest
from src import file7

class TestFile7(unittest.TestCase):
    def test_starts_with_user(self):
        self.assertTrue(file7.login("user1", "securepass"))

    def test_does_not_start_with_user(self):
        self.assertFalse(file7.login("admin", "securepass"))
