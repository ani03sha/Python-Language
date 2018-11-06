# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation
# operations on set A.
#
# Your task is to execute those operations and print the sum of elements from set A.


input()
L = set(input().split())
for _ in range(int(input())):
    command, *args = input().split()
    getattr(L, command)(set(input().split()))
print(sum(map(int, L)))
