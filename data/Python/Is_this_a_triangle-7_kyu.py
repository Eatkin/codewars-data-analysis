# https://www.codewars.com/kata/56606694ec01347ce800001b
# 2023-05-07T07:52:37.139+0000
def is_triangle(a, b, c):
    # Use triangle inequality
    return sorted([a, b, c])[-1] < sum(sorted([a, b, c])[:2])