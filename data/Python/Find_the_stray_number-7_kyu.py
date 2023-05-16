# https://www.codewars.com/kata/57f609022f4d534f05000024
# 2023-05-12T05:41:37.781+0000
def stray(arr):
    result = 0
    for elem in arr:
        result ^= elem
        
    return result