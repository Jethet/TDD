import unittest
from leap_year import leap_year

class Test_Leap_year(unittest.TestCase):

    def test_fourhundred(self):
        self.assertTrue(leap_year(1000))
        self.assertTrue(leap_year(400))

    def test_onehundred(self):
        self.assertIsNotNone(leap_year(100))
        self.assertFalse(leap_year(100))
        self.assertIsNotNone(leap_year(300))
        self.assertFalse(leap_year(300))
        self.assertIsNotNone(leap_year(1900))
        self.assertFalse(leap_year(1900))

    def test_four(self):
        self.assertTrue(leap_year(60))
        self.assertTrue(leap_year(80))
        self.assertTrue(leap_year(2020))

    def test_three(self):
        self.assertIsNotNone(leap_year(90))
        self.assertFalse(leap_year(90))
        self.assertIsNotNone(leap_year(150))
        self.assertFalse(leap_year(150))
        self.assertIsNotNone(leap_year(290))
        self.assertFalse(leap_year(290))
