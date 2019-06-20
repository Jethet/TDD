import unittest
from hello_world import hello_world

class Tests(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world("Toto"), "Hello Toto!")
