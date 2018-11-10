# You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.


import numpy

arr = input().strip().split(' ')
arr = numpy.array(arr, int)
print(numpy.reshape(arr, (3, 3)))
