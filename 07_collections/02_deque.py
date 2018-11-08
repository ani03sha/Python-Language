# Perform append, pop, popleft and appendleft methods on an empty deque d.


from collections import deque

d = deque()
for _ in range(int(input())):
    command, *argument = input().split()
    getattr(d, command)(*argument)
print(*d)
