# You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of .


import numpy

# This is just because the STUPID testcases in HackerRank has space before each element
numpy.set_printoptions(sign=' ')
a = numpy.array(input().split(), float)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))
