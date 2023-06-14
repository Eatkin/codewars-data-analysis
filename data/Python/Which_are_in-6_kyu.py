# https://www.codewars.com/kata/550554fd08b86f84fe000a58
# 2023-05-23T10:39:16.681+0000
def in_array(array1, array2):
    return sorted([word for word in set(array1) if word in " ".join(array2)])