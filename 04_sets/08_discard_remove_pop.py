# You have a non-empty set s, and you have to execute N commands given in N lines.
#
# The commands will be pop, remove and discard.


n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(0, N):
    command = input().split()
    if "pop" == command[0]:
        s.pop()
    elif "remove" == command[0]:
        s.remove(int(command[1]))
    else:
        s.discard(int(command[1]))
