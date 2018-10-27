# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and
# print the result of hash(t.
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # creating a tuple from the list
    t = tuple(list(integer_list))

    # calculating an printing the hash(t)
    print(hash(t))
