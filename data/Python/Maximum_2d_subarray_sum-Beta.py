# https://www.codewars.com/kata/585fc200db20cf20ab00018a
# 2023-05-23T13:45:04.010+0000
import numpy as np

def max_sum(arr):
    arr = np.array(arr)
    max_sum = -1
    max_subarray = []
    rows, cols = arr.shape
    
    for start_row in range(rows):
        row_sums = np.zeros(cols)
        
        for end_row in range(start_row, rows):
            row_sums += arr[end_row]
            
            # Apply Kadane's algorithm to find the maximum sum subarray in the 1D array
            current_sum = 0
            max_sum_so_far = 0
            start_col = 0
            end_col = 0
            
            for j, num in enumerate(row_sums):
                current_sum += num
                
                if current_sum < 0:
                    current_sum = 0
                    start_col = j + 1
                elif current_sum > max_sum_so_far:
                    max_sum_so_far = current_sum
                    end_col = j
            
            # Check if the current subarray has the maximum sum
            if max_sum_so_far > max_sum:
                max_sum = max_sum_so_far
                max_subarray = [start_col, start_row, end_col, end_row]
    
    return max_subarray + [max_sum]
