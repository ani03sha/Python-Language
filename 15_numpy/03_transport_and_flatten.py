# You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.


import numpy

n, m = map(int, input().split())
a = numpy.array([input().strip().split(' ') for _ in range(n)], int)
print(a.transpose())
print(a.flatten())
