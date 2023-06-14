# https://www.codewars.com/kata/5ce399e0047a45001c853c2b
# 2023-06-01T07:37:54.420+0000
def parts_sums(ls):
    if not ls:
        return [0]
    
    ls = ls[::-1]
    sums = [0]
    prev = 0
    for elem in ls:
        prev += elem
        sums.append(prev)
    
    
    return sums[::-1]