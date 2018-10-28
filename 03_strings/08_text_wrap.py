import textwrap


# You are given a string S and width w.
# Your task is to wrap the string S into a paragraph of width w.


def wrap(str, width):
    return textwrap.fill(str, width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
