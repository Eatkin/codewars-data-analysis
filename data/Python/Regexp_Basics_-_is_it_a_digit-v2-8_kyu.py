# https://www.codewars.com/kata/567bf4f7ee34510f69000032
2023-05-05T12:33:11.930+0000
import re
def is_digit(n):
    return re.fullmatch(r"\d", n) is not None