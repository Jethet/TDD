import unittest
import countRange

class TestCountRange(unittest.TestCase):

    def test_first_list(self):
        mylist = [1, 14, 23, 33]
        min_val = 2
        max_val = 26
        result = countRange.countRange(mylist, min_val, max_val)
        self.assertEqual(result, [14, 23])

if __name__ == '__main__':
    unittest.main()
