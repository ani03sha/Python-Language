# A valid email address meets the following criteria:
#
# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension The
# username starts with an English alphabetical character, and any subsequent characters consist of one or more of the
#  following: alphanumeric characters, -,., and _. The domain and extension contain only English alphabetical
# characters. The extension is 1, 3, or 3 characters in length. Given  pairs of names and email addresses as input,
# print each name and email address pair having a valid email address on a new line.


from re import match

for _ in range(int(input())):
    name, email = input().split()
    isValid = match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email)
    if isValid:
        print(name, email)
