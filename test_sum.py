# To create a simple test of get_sum(), decide what to test:
#  - can the function sum a list of whole numbers?
#  - can it sum a tuple or set:
#  - can it sum a list of floats?
#  - what happens when you provide a bad value, such as string?
#  - what happens when one of the values is negative?

# Structure of the test:
#  1. Create inputs (it is common to reuse them)
#  2. Execute code being tested, capturing the output
#  3. Compare the output with the expected result

import unittest
from fractions import Fraction
from my_sum import get_sum

class TestSum(unittest.TestCase):
    # This tests if get_sum() can sum a list of integers:
    def test_list_int(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        # This tests if get_sum() can sum a list of fractions:
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
