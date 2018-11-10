# You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of S that contains 2 or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.


import re

vowel = 'aeiou'
consonant = 'qwrtypsdfghjklzxcvbnm'
match = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonant, vowel, consonant), input(), flags=re.I)
print('\n'.join(match or ['-1']))
