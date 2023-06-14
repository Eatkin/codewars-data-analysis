# https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c
# 2023-06-05T17:47:38.716+0000
def even_numbers(arr,n):
    evens = []
    count = 0
    for num in arr[::-1]:
        if num % 2 == 0:
            count += 1
            evens.append(num)
            if count == n:
                break
                
    return evens[::-1]