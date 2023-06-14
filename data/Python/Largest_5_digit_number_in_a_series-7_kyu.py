# https://www.codewars.com/kata/51675d17e0c1bed195000001
# 2023-06-01T07:32:24.410+0000
def solution(digits):
    leading_digit = digits[0]
    largest_seen = digits[:5]
    length = len(digits)
    for i in range(1, length - 4):
        if digits[i] >= leading_digit:
            if digits[i:i + 5] > largest_seen:
                leading_digit = digits[i]
                largest_seen = digits[i:i + 5]
                
    return int(largest_seen)