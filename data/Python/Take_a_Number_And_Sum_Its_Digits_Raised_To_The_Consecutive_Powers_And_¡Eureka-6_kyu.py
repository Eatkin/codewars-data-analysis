# https://www.codewars.com/kata/5626b561280a42ecc50000d1
2023-05-12T08:43:05.896+0000
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    cache = {(n, 1): n for n in range(1, 10)}
    eureka_numbers = []
    
    for i in range(a, b + 1):
        number_split = [int(d) for d in str(i)]
        sum = 0
        for j, num in enumerate(number_split):
            power = j + 1
            if (num, power) in cache:
                sum += cache[(num, power)]
            else:
                cache[(num, power)] = num ** (power)
                sum += cache[(num, power)]
            
        if sum == i:
            eureka_numbers.append(i)
    
    return eureka_numbers