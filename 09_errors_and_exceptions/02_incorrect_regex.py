# You are given a string S.
# Your task is to find out whether S is a valid regex or not.


from re import compile

for _ in range(int(input())):
    try:
        print(bool(compile(input())))
    except:
        print('False')
