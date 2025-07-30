import unittest
from src import file6

class TestFile6(unittest.TestCase):
    def test_trimmed_input(self):
        self.assertTrue(file6.login(" admin ", " password123 "))

    def test_invalid_trim(self):
        self.assertFalse(file6.login(" user ", "wrong"))
