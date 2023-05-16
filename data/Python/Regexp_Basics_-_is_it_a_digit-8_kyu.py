# https://www.codewars.com/kata/567bf4f7ee34510f69000032
# 2023-05-05T12:31:21.645+0000
import re
def is_digit(n):
    return re.search(r"^[0-9]$", n) is not None and len(n) == 1