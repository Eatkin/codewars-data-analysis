# https://www.codewars.com/kata/55edaba99da3a9c84000003b
# 2023-05-26T20:13:13.217+0000
def divisible_by(numbers, divisor):
    return [num for num in numbers if num / divisor == num // divisor]