# https://www.codewars.com/kata/5679aa472b8f57fb8c000047
2023-05-11T09:13:26.728+0000
def find_even_index(arr):
    left = 0
    sum_left, sum_right = 0, sum(arr[left+1:])
    
    while sum_left != sum_right:
        left += 1
        # If we reach the end of the array, we haven't succeeded
        if left == len(arr):
            return -1
        
        sum_left += arr[left - 1]
        sum_right -= arr[left]
        
    return left
    