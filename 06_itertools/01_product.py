# You are given a two lists A and B. Your task is to compute their cartesian product AXB.


from itertools import product

A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(*product(A, B))
