# You are given the coefficients of a polynomial P.
# Your task is to find the value of P at point x.


import numpy

print(numpy.polyval(numpy.array(input().split(), float), float(input())))
