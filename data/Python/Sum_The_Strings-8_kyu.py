# https://www.codewars.com/kata/5966e33c4e686b508700002d
2023-05-11T19:36:11.010+0000
def sum_str(a, b):
    return str(sum([int(x) if x else 0 for x in [a, b]]))