# You are given two values a and b.
# Perform integer division and print a/b.


for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code: {}".format(e))
    except ValueError as e:
        print("Error Code: {}".format(e))
