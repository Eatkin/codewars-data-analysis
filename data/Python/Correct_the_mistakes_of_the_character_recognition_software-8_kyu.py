# https://www.codewars.com/kata/577bd026df78c19bca0002c0
2023-05-12T13:57:38.096+0000
def correct(s):
    return s.translate(str.maketrans("501", "SOI"))