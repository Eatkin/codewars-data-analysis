# https://www.codewars.com/kata/58ca658cc0d6401f2700045f
# 2023-05-24T16:16:17.413+0000
def find_multiples(integer, limit):
    return [integer * i for i in range(1, limit // integer + 1)]