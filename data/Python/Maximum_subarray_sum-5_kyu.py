# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c
# 2023-05-12T05:52:44.712+0000
def max_sequence(arr):
    if not arr:
        return 0
    
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum < 0:
            current_sum = 0
        max_sum = max(max_sum, current_sum)
        
    return max_sum