# https://www.codewars.com/kata/59831e3575ca6c8aea00003a
# 2023-06-05T14:36:50.592+0000
def game(n, m): 
    # Edge case
    if m == 2:
        return 'second'
    return 'first' if n % 2 == 1 else 'second'