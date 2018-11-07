# The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in
# combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly
# and efficiently in pure Python.
#
# You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume
# 1-based indexing) with a uniform probability from the list.
#
# Find the probability that at least one of the K indices selected will contain the letter: 'a'.


from itertools import combinations

N = int(input())
a = input().split()
K = int(input())
c = list(combinations(a, K))
result = [1 for i in range(len(c)) if 'a' in c[i]]
print(sum(result) / len(c))
