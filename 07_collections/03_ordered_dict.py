# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers bought on a particular day.
# Your task is to print each item_name and net_price in order of its first occurrence.
#
# item_name = Name of the item.
# net_price = Quantity of the item sold multiplied by the price of each item.


from collections import OrderedDict

items = OrderedDict()
for _ in range(int(input())):
    item, price = input().rsplit(' ', 1)
    items[item] = items.get(item, 0) + int(price)

for i in items:
    print(i, items[i])
