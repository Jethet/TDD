import unittest
import name_shuff

class TestNameShuff(unittest.TestCase):

    def test_name1(self):
        txt = "Rosie O'Donnell"
        result = name_shuff.name_shuffle(txt)
        self.assertEqual(result, "O'Donnell Rosie")

if __name__ == '__main__':
    unittest.main()
