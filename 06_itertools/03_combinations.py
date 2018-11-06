# You are given a string S.
# Your task is to print all possible combinations, up to size k of the string in lexicographic sorted order.


from itertools import combinations

s, k = input().split()
k = int(k)

for i in range(1, k + 1):
    for j in combinations(sorted(s), i):
        print("".join(j))
