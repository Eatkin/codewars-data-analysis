# https://www.codewars.com/kata/5552101f47fc5178b1000050
2023-03-08T14:26:51.851+0000
def dig_pow(n, p):
    # your code
    sequence = [int(num) ** (p + index) for index, num in enumerate(list(str(n)))]
    summation = sum(sequence)
    
    return summation // n if summation % n == 0 else -1