# https://www.codewars.com/kata/646254375cee7a000ffaa404
# 2023-05-23T12:07:01.983+0000
import numpy as np
def verify_latin_square(array, m):
    # For easier array operations
    try:
        array = np.array(array)
    except:
        return "Array not square"
    
    # Trivial stuff
    if array.shape[0] != array.shape[1]:
        return "Array not square"
    if array.shape[0] != m:
        return "Array is wrong size"
    
    sum_should_be = int(0.5 * m * (m + 1))
    set_of_values = set(range(1, m+1))
    # Check rows
    for row in range(array.shape[0]):
        # Detect errors
        if np.sum(array[row, :]) != sum_should_be:
            leftovers = array[row, :].tolist()
            for num in set_of_values:
                if num in leftovers:
                    leftovers.remove(num)
            if leftovers[0] in set_of_values:
                return f"{leftovers[0]} occurs more than once in row {row + 1}"
            else:
                for i, num in enumerate(array[row, :]):
                    if num == leftovers[0]:
                        return f"{leftovers[0]} at {row + 1},{i + 1} is not between 1 and {m}"
    
    # Repeat for columns
    for column in range(array.shape[1]):
        # Detect errors
        if np.sum(array[:, column]) != sum_should_be:
            leftovers = array[:, column].tolist()
            for num in set_of_values:
                if num in leftovers:
                    leftovers.remove(num)
            if leftovers[0] in set_of_values:
                return f"{leftovers[0]} occurs more than once in column {column + 1}"
            else:
                for i, num in enumerate(array[:, column]):
                    if num == leftovers[0]:
                        return f"{leftovers[0]} at {i + 1},{column + 1} is not between 1 and {m}"
    
    return f"Valid latin square of size {m}"