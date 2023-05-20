# https://www.codewars.com/kata/55208f16ecb433c5c90001d2
# 2023-05-19T20:01:55.774+0000
def trace(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return None
    
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    
    return trace