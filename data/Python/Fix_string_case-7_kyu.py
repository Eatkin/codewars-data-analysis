# https://www.codewars.com/kata/5b180e9fedaa564a7000009a
# 2023-05-20T08:28:27.697+0000
def solve(s):
    uppers = len([char for char in s if char == char.upper()])
    lowers = len(s) - uppers
    if uppers > lowers:
        return s.upper()
    
    return s.lower()