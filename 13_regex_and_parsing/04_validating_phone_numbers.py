# You are given some input, and you are required to check whether they are valid mobile numbers.
#
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.


from re import match

for _ in range(int(input())):
    if match(r'[789]\d{9}$', input()):
        print('YES')
    else:
        print('NO')
