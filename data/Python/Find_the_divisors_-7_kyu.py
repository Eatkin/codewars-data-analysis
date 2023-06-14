# https://www.codewars.com/kata/544aed4c4a30184e960010f4
# 2023-05-25T16:17:51.132+0000
def divisors(integer):
    factors = [i for i in range(2, integer // 2 + 1) if integer / i == integer // i]
    return factors if factors != [] else str(integer) + " is prime"
        