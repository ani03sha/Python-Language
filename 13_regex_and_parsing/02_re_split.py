# You are given a string s consisting only of digits 0-9, commas ,, and dots .
#
# Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the ,
# and . symbols in s.
#
# It’s guaranteed that every comma and every dot in  is preceeded and followed by a digit.


from re import split

regex_pattern = r"\D+"
print("\n".join(split(regex_pattern, input())))
