# Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
#
# One fine day, a finite number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of K members per group where K ≠ 1.
#
# The Captain was given a separate room, and the rest were given one room per group.
#
# Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of
#  the tourists. The room numbers will appear  times per group except for the Captain's room.
#
# Mr. Anant needs you to help him find the Captain's room number.
# The total number of tourists or the total number of groups of families is not known to you.
# You only know the value of  and the room number list.


K = int(input())
rooms = input().split()

rooms.sort()

# Split the list into two sets with one containing the even elements and the other the odd elements. Since the number
#  of members in a group, K, will always be greater than 1 each set contained the same room numbers except for the
# set that contained the captain's room. Then we take the symmetric difference of both sets to get the captain's room.
capt_room = (set(rooms[0::2]) ^ set(rooms[1::2]))
print(capt_room.pop())
