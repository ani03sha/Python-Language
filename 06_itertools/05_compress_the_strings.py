# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these
# consecutive occurrences of the character 'c' with (X,c) in the string.


from itertools import groupby

# Using list comprehensions, we are getting the length of occurrence of character c. x is the key i.e. character
# itself
print(*[(len(list(c)), int(x)) for x, c in groupby(input())])
