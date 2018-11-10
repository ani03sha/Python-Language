# You are given the shape of the array in the form of space-separated integers, each integer representing the size of
# different dimensions, your task is to print an array of the given shape and integer type using the tools
# numpy.zeros and numpy.ones.


import numpy

n = tuple(map(int, input().split()))
print(numpy.zeros(n, dtype=numpy.int))
print(numpy.ones(n, dtype=numpy.int))
