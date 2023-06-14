# https://www.codewars.com/kata/514b92a657cdc65150000006
# 2023-06-02T08:26:51.778+0000
import math
def solution(number):
    if number < 0:
        return 0
    
    total = 0
    interval = 30
    r = number
    # Have to reduce r by 1 because the sum is not supposed to be inclusive of r
    for s in [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30]:
        flr = math.floor((r - 1 - s) / interval)
        total += s * (flr + 1) + 0.5 * interval * flr * (flr + 1)
    return total