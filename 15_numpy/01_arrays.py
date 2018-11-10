# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.

import numpy


def arrays(a):
    a = numpy.array(a, float)
    return a[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
