# https://www.codewars.com/kata/542c0f198e077084c0000c2e
# 2023-05-12T14:30:16.188+0000
def divisors(n):
    divisor_set = {1, n}
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisor_set.add(i)
            
    return len(divisor_set)