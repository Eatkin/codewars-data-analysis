# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
# 2023-05-25T08:34:35.249+0000
def zeros(n):
    # By observation
    if n < 5:
        return 0
    zeros = 0
    power = 5
    while power < n:
        zeros += n // power
        power *= 5
    return zeros