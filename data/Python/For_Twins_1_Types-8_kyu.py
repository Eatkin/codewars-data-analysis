# https://www.codewars.com/kata/59c1302ecb7fb48757000013
# 2023-05-24T11:22:43.431+0000
import re
def type_validation(variable, _type): 
    return _type in re.search(r"'(.*)'", str(type(variable))).group(1)