# https://www.codewars.com/kata/583203e6eb35d7980400002a
# 2023-05-12T06:07:47.401+0000
import re as RegularExpressionLibrary
def count_smileys(arr):
    if not arr:
        return 0
    pattern = r"^[:;][-~]?[)D]$"
    smiley_count = 0
    for s in arr:
        if bool(RegularExpressionLibrary.match(pattern, s)):
            smiley_count += 1
    return smiley_count