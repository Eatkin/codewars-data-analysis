# https://www.codewars.com/kata/515decfd9dcfc23bb6000006
# 2023-05-24T14:24:18.584+0000
import re
def is_valid_IP(strng):
    if strng.count(".") != 3:
        return False
    invalid_chars = re.findall(r"[^0-9\.]", strng)
    if invalid_chars != []:
        return False
    
    matches = re.findall(r"\.?(\d+)\.?", strng)
    
    if len(matches) != 4:
        return False
    
    for match in matches:
        if int(match) < 0 or int(match) > 255 or match != str(int(match)):
            return False
    
    return True