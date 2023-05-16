# https://www.codewars.com/kata/566044325f8fddc1c000002c
2023-04-18T17:02:17.388+0000
def even_chars(st): 
    if len(st) < 2 or len(st) > 100:
        return "invalid string"
    
    return [char for i, char in enumerate(st) if i%2 == 1]