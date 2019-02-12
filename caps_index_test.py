import unittest
import caps_index

class TestCapsIndex(unittest.TestCase):

    def test_word(self):
        word = 'eDaBiT'
        result = caps_index.indexOfCaps(word)
        self.assertEqual(result, [1,3,5])

if __name__ == '__main__':
    unittest.main()
