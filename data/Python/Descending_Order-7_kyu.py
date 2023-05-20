# https://www.codewars.com/kata/5467e4d82edf8bbf40000155
# 2023-05-17T07:57:29.692+0000
def descending_order(num):
    return int("".join(sorted(str(num), reverse = True)))