# https://www.codewars.com/kata/5ac6932b2f317b96980000ca
# 2023-05-31T20:41:09.348+0000
def min_value(digits):
    digits = sorted(list(set(digits)))
    num = "".join([str(num) for num in digits])
    return int(num)
    