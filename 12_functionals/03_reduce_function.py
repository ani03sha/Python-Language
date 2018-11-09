# Given a list of rational numbers,find their product.


from fractions import Fraction
from functools import reduce


def product(f):
    t = reduce(lambda x, y: x * y, f)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
