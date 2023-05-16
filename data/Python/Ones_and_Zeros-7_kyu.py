# https://www.codewars.com/kata/578553c3a1b8d5c40300037c
2023-05-10T19:16:27.331+0000
def binary_array_to_number(arr):
    integer = 0
    for i, bin in enumerate(arr):
        integer += bin<<(len(arr) - i - 1)
    return integer