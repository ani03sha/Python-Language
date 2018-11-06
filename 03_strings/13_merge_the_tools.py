# Consider the following:
#
# A string, s, of length n where s=c0c1c2....cn. An integer, k, where  is a factor of n.
#
# We can split s into n/k subsegments where each subsegment, t, consists of a contiguous block of k characters in s.
# Then, use each t to create string u such that:
#
# The characters in u are a subsequence of the characters in t. Any repeat occurrence of a character is removed from
# the string such that each character in u occurs exactly once. In other words, if the character at some index j in t
#  occurs at a previous index < j in t, then do not include the character in string u.
# Given s and k, print n/k lines where each line i denotes string u.


from collections import OrderedDict


def merge_the_tools(s, k):
    # Getting the partitioned parameter
    t = len(s) // k

    for i in range(0, t):
        # Getting each substring
        temp = s[k * i:k * (i + 1)]

        # Removing duplicates and printing
        print("".join(OrderedDict.fromkeys(temp)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
