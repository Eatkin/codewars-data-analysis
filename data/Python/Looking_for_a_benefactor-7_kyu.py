# https://www.codewars.com/kata/569b5cec755dd3534d00000f
# 2023-05-30T10:43:03.746+0000
from math import ceil
def new_avg(arr, newavg):
    donation = ceil(newavg * (len(arr) + 1) - sum(arr))
    if donation < 0:
        raise ValueError
    return donation