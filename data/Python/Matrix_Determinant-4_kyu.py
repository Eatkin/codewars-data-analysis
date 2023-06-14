# https://www.codewars.com/kata/52a382ee44408cea2500074c
# 2023-05-22T05:56:56.230+0000
import numpy as np
def determinant(matrix):
    matrix = np.array(matrix)
    size = len(matrix)
    if size == 1:
        return matrix[0, 0]
    if size == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0] 
    
    # For larger ones we'll use recursion
    det = 0
    for i, num in enumerate(matrix[0]):
        sliced_matrix = np.concatenate((matrix[1:, :i], matrix[1:,i+1:]), axis=1)
        det += num * determinant(sliced_matrix) * (-1) ** (i + 2)
    
    return det
        