# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical
# characters, alphanumeric characters, digits, etc.
#
# You are given a string S. Your task is to find out if the string S
# contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
if __name__ == '__main__':
    s = input()
    print(any(x.isalnum() for x in s))
    print(any(x.isalpha() for x in s))
    print(any(x.isdigit() for x in s))
    print(any(x.islower() for x in s))
    print(any(x.isupper() for x in s))
