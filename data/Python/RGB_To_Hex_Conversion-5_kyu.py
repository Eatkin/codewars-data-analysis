# https://www.codewars.com/kata/513e08acc600c94f01000001
# 2023-05-26T20:17:39.963+0000
def rgb(r, g, b):
    return "".join(hex(min(255, max(0, c))).split('x')[1].rjust(2, '0').upper() for c in [r, g, b])