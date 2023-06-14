# https://www.codewars.com/kata/56f699cd9400f5b7d8000b55
# 2023-05-24T16:10:57.066+0000
def fix_the_meerkat(arr):
    arr[0], arr[2] = arr[2], arr[0]
    return arr