# You are given a 2-D array of size NXM.
# Your task is to find:
#
# The mean along axis 0
# The var along axis 1
# The std along axis None


import numpy

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(numpy.std(a))
