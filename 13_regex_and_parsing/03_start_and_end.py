# You are given a string S.
# Your task is to find the indices of the start and end of string k in S.


from re import finditer

s, k = input(), input()
m = list(finditer(r'(?={})'.format(k), s))
if m:
    print('\n'.join(str((match.start(), match.start() + len(k) - 1)) for match in m))
else:
    print('(-1, -1)')
