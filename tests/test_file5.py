import unittest
from src import file5

class TestFile5(unittest.TestCase):
    def test_in_mock_db(self):
        self.assertTrue(file5.login("admin", "password123"))

    def test_not_in_db(self):
        self.assertFalse(file5.login("user3", "test"))
