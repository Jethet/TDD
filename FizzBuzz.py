
import unittest

def fizzbuzz(*args):
    for x in args:

        if x % 3 == 0 and x % 5 == 0:
            #print("FizzBuzz")
            return "FizzBuzz"

        elif x % 3 == 0:
            #print("Fizz")
            return "Fizz"

        elif x % 5 == 0:
            #print("Buzz")
            return "Buzz"

        else:
            print(x)

fizzbuzz()


class Test_Fizzbuzz(unittest.TestCase):
    def setUp(self):
        pass

    def test_Fizz(self):
        expected = "Fizz"
        self.assertEqual(expected, fizzbuzz(3))

    def test_Buzz(self):
        expected = "Buzz"
        self.assertEqual(expected, fizzbuzz(5))

    def test_FizzBuzz(self):
        expected = "FizzBuzz"
        self.assertEqual(expected, fizzbuzz(15))

if __name__ == '__main__':
    unittest.main()
