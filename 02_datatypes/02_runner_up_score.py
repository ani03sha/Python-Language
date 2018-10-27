# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input("Enter the number of elements"))
    arr = map(int, input("Enter the scores").split())

    # Converting map to list
    my_list = list(arr)

    # Sorting the list in ascending order
    my_list.sort()

    # Getting the length of the list
    length = len(my_list)

    # The second condition in this loop handles the case of similar elements
    while length > 0 and my_list[length - 1] == my_list[length - 2]:
        length -= 1

    # Printing the list
    print(my_list[length - 2])
