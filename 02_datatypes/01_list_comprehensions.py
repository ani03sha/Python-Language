# You are given three integers X, Y and Z representing the dimensions of a cuboid along with an integer N. You have to
# print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of (i+j+k) is not equal to N.
if __name__ == '__main__':
    x = int(input("Enter the x dimension\n"))
    y = int(input("Enter the y dimension\n"))
    z = int(input("Enter the z dimension\n"))
    n = int(input("Enter the limit\n"))

    # List comprehension
    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j + k) != n)])
