# https://www.codewars.com/kata/558fc85d8fd1938afb000014
2023-04-18T16:49:48.553+0000
def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))