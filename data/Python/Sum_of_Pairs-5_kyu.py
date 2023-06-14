# https://www.codewars.com/kata/54d81488b981293527000c8f
# 2023-05-24T12:20:27.088+0000
def sum_pairs(ints, s):
    seen = {}
    for n in ints:
        diff = s - n
        if diff in seen:
            return [diff, n]
        if n not in seen:
            seen[n] = 1 # we don't actually care about the index so 1 is arbitrary

    return None