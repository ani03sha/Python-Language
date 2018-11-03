# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference
# indicates those values that exist in either M or N but do not exist in both.


# Reading the values from console
a, b = (int(input()), input().split())
c, d = (int(input()), input().split())

# Assigning values to two sets
x = set(b)
y = set(d)

# Finding the elements which are in y but not in x
p = y.difference(x)

# Finding the elements which are in x but not in y
q = x.difference(y)

# Union all values
r = p.union(q)

# Print the values in ascending order
print('\n'.join(sorted(r, key=int)))
