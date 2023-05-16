# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e
# 2023-05-14T12:58:45.199+0000
def two_sort(array):
    return "***".join(sorted(array, key = lambda x: tuple(ord(i) for i in x))[0])