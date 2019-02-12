"""
Python’s standard library includes a method named count that determines how
many times a specific value occurs in a list. In this exercise, you will create
a new function named countRange which determines and returns the number of
elements within a list that are greater than or equal to some minimum value
and less than some maximum value. Your function will take three parameters:
the list, the minimum value and the maximum value. It will return an integer
result greater than or equal to 0. Include a main program that demonstrates
your function for several different lists, minimum values and maximum values.
Ensure that your program works correctly for both lists of integers and
lists of floating point numbers.

"""

def countRange(mylist, min_val, max_val):
    list_values = []
    for num in mylist:
        if num >= min_val and num < max_val:
            list_values.append(num)
    return list_values


print(countRange([1, 14, 23, 33], 2, 26))
