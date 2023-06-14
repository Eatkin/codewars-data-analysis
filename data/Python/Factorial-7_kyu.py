# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc
# 2023-05-25T07:43:31.698+0000
def factorial(n):
    if n < 0:
        raise ValueError("You fucking idiot you can't factorial a negative number")
    if n > 12:
        raise ValueError("I dunno the Kata saying you can't factorial a number above 12 for some reason")
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)