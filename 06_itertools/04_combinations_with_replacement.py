# You are given a string S.
# Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.


from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)
for i in combinations_with_replacement(sorted(s), k):
    print("".join(i))
