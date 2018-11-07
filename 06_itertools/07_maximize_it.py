from itertools import product

K, M = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
Y = map(lambda X: sum(i ** 2 for i in X) % M, product(*N))
print(max(Y))
