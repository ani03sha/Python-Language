# Apply your knowledge of the .add() operation to help your friend Rupal.
#
# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in
# her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
#
# Find the total number of distinct country stamps.


# Reading the number of country stamps
N = int(input())

# Initializing a set
stamps = set()

# Iterating the loop to add input values in the set
for i in range(0, N):
    stamps.add(input())

# Printing the length of the set
print(len(stamps))
