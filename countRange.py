"""
Python’s standard library includes a method named count that determines how
many times a specific value occurs in a list. In this exercise, you will create a new
function named countRange which determines and returns the number of elements
within a list that are greater than or equal to some minimum value and less than some
maximum value. Your function will take three parameters: the list, the minimum
value and the maximum value. It will return an integer result greater than or equal to
0. Include a main program that demonstrates your function for several different lists,
minimum values and maximum values. Ensure that your program works correctly
for both lists of integers and lists of floating point numbers.

max()			returns the biggest value in a list
min()			returns the smallest value in a list
alist.count(input)
"""
import unittest

def countRange():
    mylist = []
    min_value = 'a'
    max_value = 'b'
    for x in mylist:
        print(mylist.count(x >= 'a' and < 'b'))

countRange()

class Test_countRange(unittest.TestCase):
    def setUp(self):
        pass

    def test_countMin(self):
        expected =
