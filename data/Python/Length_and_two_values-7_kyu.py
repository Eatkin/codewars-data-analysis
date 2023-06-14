# https://www.codewars.com/kata/62a611067274990047f431a8
# 2023-05-24T14:15:49.013+0000
import numpy as np
def alternate(n, first_value, second_value):
    a = np.array([first_value, second_value], dtype=object)
    return np.tile(a, n).tolist()[:n]
