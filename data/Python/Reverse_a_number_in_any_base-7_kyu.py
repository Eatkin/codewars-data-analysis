# https://www.codewars.com/kata/6469e4c905eaefffd44b6504
# 2023-05-23T08:44:09.578+0000
def reverse_number(n, b):
    if b == 0 or n == 0:
        return 0
    if b == 1:
        return n
    digits = []
    while n:
        digits.append(n % b)
        n //= b
    string_repr = ""
    
    for digit in digits:
        string_repr += str(digit) if digit < 10 else chr(ord('A') + digit - 10)
    
    significance = 1
    accumulator = 0
    for char in string_repr[::-1]:
        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            accumulator += significance * int(char)
        else:
            accumulator += significance * (ord(char) + 10 - ord('A'))
        
        significance *= b
            
    return accumulator