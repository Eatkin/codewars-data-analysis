# https://www.codewars.com/kata/5571f712ddf00b54420000ee
# 2023-04-20T17:42:14.126+0000
import math
def loose_change(cents):
    cents = max(0, math.floor(cents))
    
    change = [("Quarters", 25), ("Dimes", 10), ("Nickels", 5), ("Pennies", 1)]
    change_dict = {}
    
    for coin, value in change:
        change_dict[coin] = cents // value
        cents -= change_dict[coin] * value
    
    return change_dict