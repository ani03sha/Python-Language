# You are given two arrays: A and B.
# Your task is to compute their inner and outer product.


import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)
print(numpy.inner(a, b), numpy.outer(a, b), sep='\n')
