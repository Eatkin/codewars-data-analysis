# https://www.codewars.com/kata/52c31f8e6605bcc646000082
# 2023-05-11T05:06:23.259+0000
def two_sum(numbers, target):
    cache = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in cache:
            return [cache[complement], i]
        cache[num] = i
    
    return [-1, -1]