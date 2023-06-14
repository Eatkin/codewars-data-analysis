# https://www.codewars.com/kata/55c6126177c9441a570000cc
# 2023-05-25T07:54:31.308+0000
def order_weight(strng):
    def sum_digits(s):
        sum = 0
        for char in s:
            sum += int(char)
        return sum
    
    return " ".join(sorted(strng.split(), key=lambda x: (sum_digits(x), x)))