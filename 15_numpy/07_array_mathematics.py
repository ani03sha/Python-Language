# You are given two integer arrays, A and B of dimensions NXM.
# Your task is to perform the following operations:
#
# Add ( A+B )
# Subtract ( A-B )
# Multiply ( A*B )
# Integer Division ( A/B )
# Mod ( A%B )
# Power ( A**B )


import numpy

n, m = list(map(int, input().split()))

a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(*[eval('a' + i + 'b') for i in ['+', '-', '*', '//', '%', '**']], sep='\n')
