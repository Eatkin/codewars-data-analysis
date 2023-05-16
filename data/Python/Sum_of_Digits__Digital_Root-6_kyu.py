# https://www.codewars.com/kata/541c8630095125aba6000c00
# 2023-04-20T17:29:07.363+0000
def digital_root(n):
    # Explode the number
    digits = [int(n) for n in str(n)]
    while len(digits) > 1:
        digits = [int(n) for n in str(sum(digits))]
        
    return digits[0]