# You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the
# root as 0.


import xml.etree.ElementTree as etree

max_depth = 0


def depth(elem, level):
    global max_depth
    # your code goes here
    level += 1
    if level >= max_depth:
        max_depth = level
    for child in elem:
        depth(child, level)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(max_depth)
