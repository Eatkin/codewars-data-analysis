# https://www.codewars.com/kata/55aa075506463dac6600010d
2023-03-08T19:40:01.996+0000
from math import sqrt
from functools import reduce

def list_squared(m, n):
    # your code
    squares = []
    for num in range(m, n + 1):
        # Code graciously borrowed from stackoverflow (otherwise it's too slow)
        # https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
        divisors = set(reduce(list.__add__, 
                ([i ** 2, (num//i) ** 2] for i in range(1, int(num**0.5) + 1) if num % i == 0)))
        if sqrt(sum(divisors)).is_integer():
            squares.append([num, sum(divisors)])
    
    return squares
    pass