# https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023
2023-05-05T12:13:20.233+0000
import re

def validate_usr(username):
    regex = re.compile(r"^[a-z0-9_]{4,16}$")
    res =  re.match(regex, username)
    return res is not None