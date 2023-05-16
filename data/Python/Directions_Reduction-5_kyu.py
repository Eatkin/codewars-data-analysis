# https://www.codewars.com/kata/550f22f4d758534c1100025a
2023-05-07T08:57:16.048+0000
import re

def dirReduc(arr):
    new_directions = re.sub(r"NORTH\sSOUTH|SOUTH\sNORTH|EAST\sWEST|WEST\sEAST", "", " ".join(arr)).split()
    if arr != new_directions:
        new_directions = dirReduc(new_directions)
    
    return new_directions