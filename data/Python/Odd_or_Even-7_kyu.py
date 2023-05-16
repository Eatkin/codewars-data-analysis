# https://www.codewars.com/kata/5949481f86420f59480000e7
2023-05-11T13:31:08.518+0000
def odd_or_even(arr):
    return "even" if len([x for x in arr if x % 2 == 1]) % 2 == 0 else "odd"