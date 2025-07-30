import unittest
from src import file8

class TestFile8(unittest.TestCase):
    def test_valid_login(self):
        file8.attempts = {}
        self.assertTrue(file8.login("admin", "password123"))

    def test_lock_after_3_attempts(self):
        file8.attempts = {}
        for _ in range(3):
            file8.login("admin", "wrong")
        self.assertEqual(file8.login("admin", "wrong"), "Account locked")
