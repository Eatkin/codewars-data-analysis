# https://www.codewars.com/kata/5779624bae28070489000146
# 2023-06-05T14:56:48.813+0000
import numpy as np
def logistic_map(width,height,xs,ys):
    # Edge case
    if xs == [] and ys == []:
        arr = []
        for i in range(height):
            temp = []
            for j in range(width):
                temp.append(None)
            arr.append(temp)
        return arr
    
    arr = np.zeros([height, width])
        
    # Just measure distance from xs and ys
    for i in range(height):
        for j in range(width):
            # Minimise distance
            min_value = width * height  # first maximise distance
            for k in range(len(xs)):
                min_value = min(min_value, abs(xs[k] - j) + abs(ys[k] - i))
            arr[i, j] = min_value
            
    print(arr)
    return arr.tolist()