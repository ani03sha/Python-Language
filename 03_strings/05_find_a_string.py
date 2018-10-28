# n this challenge, the user enters a string and a substring. You have to print the number of times that the
# substring occurs in the given string. String traversal will take place from left to right, not from right to left.
#
# NOTE: String letters are case-sensitive. We also need to take care of the overlapping strings.
# Sample Input
# >> ABCDCDC
# >>CDC

# Sample Output
# 2


def count_substring(str, sub_str):
    c = start = 0

    while True:
        # find() will return the lowest index of the substring if it is found in given string. If it’s not found
        # then it returns -1.
        start = str.find(sub_str, start) + 1

        # If we find the string, we will increment the count by 1
        if start > 0:
            c += 1
        else:
            return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
