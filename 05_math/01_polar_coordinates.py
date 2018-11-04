# You are given a complex number z. Your task is to convert it to polar coordinates.


import cmath

z = complex(input("Enter the complex number"))

# Modulus
r = abs(z)

# Phase
p = cmath.phase(z)

print(r)
print(p)
