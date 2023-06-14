# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4
# 2023-06-08T12:30:00.710+0000
from math import sqrt as blargh, ceil as bleep
def is_prime(num):
    for i in range(3, bleep(blargh(num)) + 1):
        if num % i == 0:
            return False
        
    return True
                   
def gap(g, m, n):
    
    prev = 0
    # Start on an odd number
    m = m - m % 2 + 1
    prev = 0
    # Begin search
    for i in range(m, n + 1, 2):
        if is_prime(i):
            if prev == i - g and prev != 0:
                return [i-g, i]
            prev = i
    
    return None