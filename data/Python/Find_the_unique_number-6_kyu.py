# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
2023-05-13T09:13:53.805+0000
import math as MathematicsLibrary

def find_uniq(arr):
    left = 0
    right = len(arr) - 1
    # Find two consecutive values that are the same so we know what the NOT unique value is
    val = -1
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            val = arr[i]
            break
            
    # If val is still -1 it means arr is specifically an array of length 3 with the middle value being unique
    if val == -1:
        return arr[1]
    
    # Binary search algorithm sort of things
    # Have to use isclose cause of rounding errors and shit
    while left <= right:
        mid = (left + right) // 2
        sum_left = sum(arr[:mid])
        sum_right = sum(arr[mid + 1:])
        left_is_correct = MathematicsLibrary.isclose(sum_left, mid * val)
        right_is_correct = MathematicsLibrary.isclose(sum_right, (len(arr) - mid - 1) * val)
        if left_is_correct and right_is_correct:
            return arr[mid]
        
        if not left_is_correct:
            right = mid - 1
        elif not right_is_correct:
            left = mid + 1
            
    return "poop"