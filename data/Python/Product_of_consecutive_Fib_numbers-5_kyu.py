# https://www.codewars.com/kata/5541f58a944b85ce6d00006a
# 2023-05-17T07:06:23.997+0000
from math import sqrt, ceil
def generate_fibs(max_value):
    fibs = [0, 1, 1]
    # We add an extra one because we need it
    while fibs[-2] < max_value:
        n = len(fibs)
        fibs.append(fibs[n - 2] + fibs[n - 1])
    
    # We actually only need the last 3
    return fibs[-3:]

def productFib(prod):
    if prod < 0:
        return "fuck off"
    
    max_fib = ceil(sqrt(prod))
    
    fibs = generate_fibs(max_fib)
    product = [fibs[0] * fibs[1], fibs[1] * fibs[2]]
    
    # A bit messy but hey it works just fine
    if product[0] == prod:
        return [fibs[0], fibs[1], True]
    elif product[1] == prod:
        return [fibs[1], fibs[2], True]
    elif product[0] > prod:
        return [fibs[0], fibs[1], False]
    
    return [fibs[1], fibs[2], False]