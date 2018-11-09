# You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then, apply the map
# function and a lambda expression to cube each fibonacci number and print the list.


cube = lambda x: x ** 3


def fibonacci(n):
    a = [0, 1]
    for i in range(2, n):
        a.append(a[i - 1] + a[i - 2])
    return a[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
