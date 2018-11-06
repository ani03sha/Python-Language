# You are given a string S.
# Your task is to print all possible permutations of size k of the string in lexicographic sorted order.


from itertools import permutations

s, k = input().split()
k = int(k)
p = list(permutations(s, k))
p.sort()

for i in p:
    print("".join(i))
