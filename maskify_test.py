import unittest
import maskify

class TestMaskify(unittest.TestCase):

    def test_number(self):
        txt = "4556364607935616"
        result = maskify.maskify(txt)
        self.assertEqual(result, "############5616")

if __name__ == '__main__':
    unittest.main()
