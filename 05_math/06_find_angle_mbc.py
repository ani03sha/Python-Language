# ABC is a right triangle, 90 degree at B.
# Therefore, angleABC = 90 degree.
#
# Point M is the midpoint of hypotenuse .
#
# You are given the lengths AB and BC.
# Your task is to find  angleMBC in degrees.
#
# Input Format
#
# The first line contains the length of side AB.
# The second line contains the length of side BC.


import math

AB = float(input())
BC = float(input())

# Hypotenuse of triangle ABC
AC = math.hypot(AB, BC)

# Calculating the angle using cosine formula
angleMBC = round(math.degrees(math.acos(BC / AC)))

# Degree symbol
degree = chr(176)

print(angleMBC, degree, sep='')
