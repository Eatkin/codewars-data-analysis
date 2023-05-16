# https://www.codewars.com/kata/57a37f3cbb99449513000cd8
# 2023-05-05T12:49:03.120+0000
import re
def get_number_from_string(string):
    return int(re.sub(r"\D", "", string))