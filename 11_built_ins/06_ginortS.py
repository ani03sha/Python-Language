# You are given a string S.
# S contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.


def getresult(x):
    if x.islower():
        return 1, x
    elif x.isupper():
        return 2, x
    elif x.isdigit():
        if int(x) % 2 == 1:
            return 3, x
        else:
            return 4, x


print(*sorted(input(), key=getresult), sep='')
