# You will be given 2 integers, n and m. There are n words, which might repeat, in word group A. There are m words
# belonging to word group B. For each  words, check whether the word has appeared in group A or not. Print the indices
# of each occurrence of m in group A. If it does not appear, print -1.


from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(1, n + 1):
    d[input()].append(str(i))
for i in range(m):
    print(' '.join(d[input()]) or -1)
