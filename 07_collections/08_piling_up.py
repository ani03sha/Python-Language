# There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of
# cubes. The new pile should follow these directions: if CUBEi is on top of CUBEj then SIDELENGTHj > SIDELENGTHi.
#
# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if
# it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.


from collections import deque

for i in range(int(input())):
    _, n = input(), deque(map(int, input().split()))
    result = True

    for j in range(len(n) - 1):
        if n[0] >= n[1]:
            n.popleft()
        elif n[-1] >= n[-2]:
            n.pop()
        else:
            result = False
            break

    print('Yes' if result else 'No')
