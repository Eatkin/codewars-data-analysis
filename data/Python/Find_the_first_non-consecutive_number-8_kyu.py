# https://www.codewars.com/kata/58f8a3a27a5c28d92e000144
# 2023-05-12T09:02:31.166+0000
def first_non_consecutive(arr):
    if len(arr) < 2:
        return None
    
    # Time for a totally unnecessary binary search algorithm
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (right + left) // 2
        if arr[mid] != arr[mid-1] + 1 and mid != 0:
            return arr[mid]
        elif arr[mid] != arr[mid+1] - 1 and mid != len(arr) - 1:
            return arr[mid + 1]
        
        if arr[mid] == arr[0] + mid:
            left = mid + 1
        else:
            right = mid - 1
    
    return None