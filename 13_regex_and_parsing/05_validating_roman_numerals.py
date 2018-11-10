# You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True.
# Otherwise, print False. Try to create a regular expression for a valid Roman numeral.


from re import match

# Breaking it down:
#
# M{0,4}
#
# This specifies the thousands section and basically restrains it to between 0 and 4000. It's a relatively simple:
#
#    0: <empty>  matched by M{0}
# 1000: M        matched by M{1}
# 2000: MM       matched by M{2}
# 3000: MMM      matched by M{3}
# 4000: MMMM     matched by M{4}
# (CM|CD|D?C{0,3})
#
# Slightly more complex, this is for the hundreds section and covers all the possibilities:
#
#   0: <empty>  matched by D?C{0} (with D not there)
# 100: C        matched by D?C{1} (with D not there)
# 200: CC       matched by D?C{2} (with D not there)
# 300: CCC      matched by D?C{3} (with D not there)
# 400: CD       matched by CD
# 500: D        matched by D?C{0} (with D there)
# 600: DC       matched by D?C{1} (with D there)
# 700: DCC      matched by D?C{2} (with D there)
# 800: DCCC     matched by D?C{3} (with D there)
# 900: CM       matched by CM
# (XC|XL|L?X{0,3})
#
# Same rules as previous section but for the tens place:
#
#  0: <empty>  matched by L?X{0} (with L not there)
# 10: X        matched by L?X{1} (with L not there)
# 20: XX       matched by L?X{2} (with L not there)
# 30: XXX      matched by L?X{3} (with L not there)
# 40: XL       matched by XL
# 50: L        matched by L?X{0} (with L there)
# 60: LX       matched by L?X{1} (with L there)
# 70: LXX      matched by L?X{2} (with L there)
# 80: LXXX     matched by L?X{3} (with L there)
# 90: XC       matched by XC
# (IX|IV|V?I{0,3})
#
# This is the units section, handling 0 through 9 and also similar to the previous two sections (Roman numerals,
# despite their seeming weirdness, follow some logical rules once you figure out what they are):
#
# 0: <empty>  matched by V?I{0} (with V not there)
# 1: I        matched by V?I{1} (with V not there)
# 2: II       matched by V?I{2} (with V not there)
# 3: III      matched by V?I{3} (with V not there)
# 4: IV       matched by IV
# 5: V        matched by V?I{0} (with V there)
# 6: VI       matched by V?I{1} (with V there)
# 7: VII      matched by V?I{2} (with V there)
# 8: VIII     matched by V?I{3} (with V there)
# 9: IX       matched by IX
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
print(str(bool(match(regex_pattern, input()))))
