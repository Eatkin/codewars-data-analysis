# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058
# 2023-05-23T07:07:30.904+0000
import re
def solve(s):
    uppers = re.sub("[^A-Z]", "", s)
    lowers = re.sub("[^a-z]", "", s)
    numbers = re.sub("[^\d]", "", s)
    specials = re.sub("[A-Z0-9]", "", s, flags=re.IGNORECASE)
    return [len(uppers), len(lowers), len(numbers), len(specials)]