# https://www.codewars.com/kata/5526fc09a1bbd946250002dc
2023-03-08T09:38:39.639+0000
def find_outlier(integers):
    evens = []
    odds = []
    for n in integers:
        if n%2 == 0:
            evens.append(n)
            continue
        odds.append(n)
    return evens[0] if len(evens) < len(odds) else odds[0]