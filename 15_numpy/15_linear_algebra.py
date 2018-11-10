# You are given a square matrix A with dimensions NXN. Your task is to find the determinant.


import numpy

a = numpy.array([input().split() for _ in range(int(input()))], float)
numpy.set_printoptions(legacy='1.13')
print(round(numpy.linalg.det(a)))
