# Your task is to print an array of size NXM with its main diagonal elements as 1's and 0's everywhere else.


import numpy

# The replace function is just because the STUPID test cases in HackerRank problems contain an extra space
print(str(numpy.eye(*map(int, input().split()))).replace('1', ' 1').replace('0', ' 0'))
