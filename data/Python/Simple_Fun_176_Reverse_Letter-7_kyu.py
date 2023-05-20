# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b
# 2023-05-17T06:39:24.274+0000
import re
def reverse_letter(string):
    return re.sub(r"[^a-zA-Z]", "", string[::-1])