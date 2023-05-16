# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
2023-05-13T09:14:32.963+0000
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b