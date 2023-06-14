# https://www.codewars.com/kata/55466989aeecab5aac00003e
# 2023-06-06T13:41:40.155+0000
def sq_in_rect(lng, wdth, depth = 1):
    if lng == wdth:
        if depth == 1:
            return None
        return [lng]
    
    squares = [min(lng, wdth)]
    if lng > wdth:
        lng -= wdth
    else:
        wdth -= lng

    if lng !=0 or wdth !=0:
        squares += sq_in_rect(lng, wdth, depth+1)
        
    return squares