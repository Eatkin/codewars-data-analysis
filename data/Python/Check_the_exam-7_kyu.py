# https://www.codewars.com/kata/5a3dd29055519e23ec000074
2023-05-14T13:02:41.930+0000
def check_exam(arr1,arr2):
    return max(0, sum([4 if arr1[i] == arr2[i] else (0 if arr2[i] == "" else -1) for i in range(len(arr1))]))