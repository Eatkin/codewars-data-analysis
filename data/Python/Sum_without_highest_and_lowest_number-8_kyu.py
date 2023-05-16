# https://www.codewars.com/kata/576b93db1129fcf2200001e6
2023-05-11T13:29:54.099+0000
def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0
    arr.pop(arr.index(max(arr)))
    arr.pop(arr.index(min(arr)))
    return sum(arr)