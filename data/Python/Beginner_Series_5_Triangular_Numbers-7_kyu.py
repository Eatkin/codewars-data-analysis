# https://www.codewars.com/kata/56d0a591c6c8b466ca00118b
# 2023-05-23T07:17:49.740+0000
from math import ceil
def is_triangular(t):
    # Binary search
    max_n = ceil(t / 2)
    
    left = 0
    right = max_n
    while left <= right:
        mid = (left + right) // 2
        test_t = 0.5 * mid * (mid + 1)
        if test_t == t:
            return True
        
        if test_t < t:
            left = mid + 1
        else:
            right = mid - 1
    
    return False