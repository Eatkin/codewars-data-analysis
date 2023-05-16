# https://www.codewars.com/kata/556deca17c58da83c00002db
2023-05-12T07:26:47.171+0000
def tribonacci(signature, n):
    if n <= 3:
        return signature[:n]
    
    a = 3
    rolling_sum = sum(signature)
    while a < n:
        signature.append(rolling_sum)
        rolling_sum *= 2
        rolling_sum -= signature[-4]
        a += 1
    
    return signature