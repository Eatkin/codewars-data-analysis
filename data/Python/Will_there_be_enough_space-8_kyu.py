# https://www.codewars.com/kata/5875b200d520904a04000003
# 2023-05-12T10:12:09.509+0000
def enough(cap, on, wait):
    return max(0, wait - cap + on)