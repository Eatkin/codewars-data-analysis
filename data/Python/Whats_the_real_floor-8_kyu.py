# https://www.codewars.com/kata/574b3b1599d8f897470018f6
# 2023-05-17T08:01:24.147+0000
def get_real_floor(n):
    real_floor = n
    if real_floor <= 0:
        return real_floor
    if real_floor > 0:
        real_floor -= 1
    if real_floor >= 13:
        real_floor -= 1
    
    return real_floor