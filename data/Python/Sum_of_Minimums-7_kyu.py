# https://www.codewars.com/kata/5d5ee4c35162d9001af7d699
# 2023-05-22T09:44:43.275+0000
def sum_of_minimums(numbers):
    return sum([min(arr) for arr in numbers])