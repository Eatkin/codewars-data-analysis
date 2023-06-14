# https://www.codewars.com/kata/5f70c883e10f9e0001c89673
# 2023-05-26T16:30:24.463+0000
def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a)[::-1]