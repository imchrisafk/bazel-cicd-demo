import unittest
from hello import greet


class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World!")

    def test_greet_empty(self):
        self.assertEqual(greet(""), "Hello, !")
