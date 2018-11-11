# A valid postal code P have to fulfill both below requirements:
#
# P must be a number in the range from 100000 to 999999 inclusive. P must not contain more than one alternating
# repetitive digit pair. Alternating repetitive digits are digits which repeat immediately after the next digit. In
# other words, an alternating repetitive digit pair is formed by two equal digits that have just a single digit
# between them.
#
# For example:
#
# 121426 # Here, 1 is an alternating repetitive digit. 523563 # Here, NO digit is an alternating repetitive digit.
# 552523 # Here, both 2 and 5 are alternating repetitive digits. Your task is to provide two regular expressions
# regex_integer_in_range and regex_alternating_repetitive_digit_pair. Where:
#
# regex_integer_in_range should match only integers range from 100000 to 999999 inclusive
#
# regex_alternating_repetitive_digit_pair should find alternating repetitive digits pairs in a given string.
#
# Both these regular expressions will be used by the provided code template to check if the input string  is a valid
# postal code using the following expression:
#
# (bool(re.match(regex_integer_in_range, P))
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


import re

s = input()
print(bool(re.match(r'^[1-9][\d]{5}$', s) and len(re.findall(r'(\d)(?=\d\1)', s)) < 2))
