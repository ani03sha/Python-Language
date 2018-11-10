# You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence
# from top to bottom.
#
# CSS Code Pattern
#
# Selector
# {
# 	Property: Value;
# }


import re
import sys

[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]
