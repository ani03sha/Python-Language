# You are given an HTML code snippet of N lines.
# Your task is to print start tags, end tags and empty tags separately.
#
# Format your results in the following way:
#
# Start : Tag1 End   : Tag1 Start : Tag2 -> Attribute2[0] > Attribute_value2[0] -> Attribute2[1] > Attribute_value2[
# 1] -> Attribute2[2] > Attribute_value2[2] Start : Tag3 -> Attribute3[0] > None Empty : Tag4 -> Attribute4[0] >
# Attribute_value4[0] End   : Tag3 End   : Tag2 Here, the -> symbol indicates that the tag contains an attribute. It
# is immediately followed by the name of the attribute and the attribute value. The > symbol acts as a separator of
# the attribute and the attribute value.
#
# If an HTML tag has no attribute then simply print the name of the tag.
# If an attribute has no attribute value then simply print the name of the attribute value as None.
#
# Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments
# -->).Comments can be multiline as well.


from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start : ', tag)
        for i in attrs:
            print('->', i[0], '>', i[1])

    def handle_endtag(self, tag):
        print('End :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for i in attrs:
            print('->', i[0], '>', i[1])


customParser = CustomHTMLParser()
for _ in range(int(input())):
    customParser.feed(input())
