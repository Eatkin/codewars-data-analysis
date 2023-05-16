# https://www.codewars.com/kata/56a946cd7bd95ccab2000055
# 2023-05-05T12:54:03.589+0000
import re
def lowercase_count(string):
    return len(re.findall(r"[a-z]", string))