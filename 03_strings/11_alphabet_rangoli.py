# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk
# art based on creation of patterns.)
#
# Different sizes of alphabet rangoli are shown below:
#
# #size 3
#
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
#
# #size 5
#
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
#
# #size 10
#
# ------------------j------------------ ----------------j-i-j---------------- --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------ ----------j-i-h-g-f-g-h-i-j---------- --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------ ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j---- --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j-- ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------ --------j-i-h-g-f-e-f-g-h-i-j-------- ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------ --------------j-i-h-i-j-------------- ----------------j-i-j----------------
# ------------------j------------------ The center of the rangoli has the first alphabet letter a, and the boundary
# has the Nth alphabet letter (in alphabetical order).


import string


def print_rangoli(number):
    alpha = string.ascii_lowercase

    L = []
    for i in range(number):
        s = "-".join(alpha[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print('\n'.join(L[:0:-1] + L))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
