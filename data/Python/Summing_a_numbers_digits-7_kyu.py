# https://www.codewars.com/kata/52f3149496de55aded000410
# 2023-05-17T08:02:25.972+0000
def sum_digits(number):
    return sum([int(dig) for dig in str(number).lstrip("-")]) 