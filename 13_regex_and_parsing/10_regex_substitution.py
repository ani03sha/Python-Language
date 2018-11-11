# You are given a text of N lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following:
#
# && → and
# || → or
# Both && and || should have a space " " on both sides.


from re import sub

for _ in range(int(input())):
    print(sub(r'(?<= )(&&|\|\|)(?= )', lambda l: 'and' if l.group() == '&&' else 'or', input()))
