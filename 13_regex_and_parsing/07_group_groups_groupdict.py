# You are given a string S. Your task is to find the first occurrence of an alphanumeric character in S (read from
# left to right) that has consecutive repetitions.


from re import search

m = search(r"([a-z0-9])\1+", input())
print(m.group(1) if m else -1)
