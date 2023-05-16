# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
2023-05-12T10:41:08.635+0000
import re
def abbrev_name(name):
    return ".".join(re.findall(r"\b(\w)", name)).upper()
    