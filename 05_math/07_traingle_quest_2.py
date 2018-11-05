# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.
#
# For example, a palindromic triangle of size 5 is:
#
# 1
# 121
# 12321
# 1234321
# 123454321
#
# You can't take more than two lines.


for i in range(1, int(input()) + 1):
    print(pow(((pow(10, i) - 1) // 9), 2))
