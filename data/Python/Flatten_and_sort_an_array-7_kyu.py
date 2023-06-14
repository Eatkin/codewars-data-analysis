# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f
# 2023-05-25T16:26:33.770+0000
import numpy as numerical_python_library
def flatten_and_sort(array):
    try:
        return sorted(numerical_python_library.concatenate([sublist for sublist in array]).tolist())
    except:
        return []