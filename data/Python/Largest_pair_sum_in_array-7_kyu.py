# https://www.codewars.com/kata/556196a6091a7e7f58000018
# 2023-05-20T08:21:22.112+0000
def largest_pair_sum(numbers): 
    sum = max(numbers)
    numbers.pop(numbers.index(max(numbers)))
    return max(numbers) + sum