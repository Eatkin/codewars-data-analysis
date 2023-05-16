# https://www.codewars.com/kata/52c31f8e6605bcc646000082
# 2023-05-10T18:44:29.657+0000
def two_sum(numbers, target):
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers[i+1:]):
            if a + b == target:
                return [i, i + j + 1]
    return -1