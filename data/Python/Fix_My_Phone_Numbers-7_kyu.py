# https://www.codewars.com/kata/596343a24489a8b2a00000a2
# 2023-05-05T12:57:32.906+0000
import re
def is_it_a_num(s: str) -> str:
    cleaned_num = re.sub(r"\D", "", s)
    return cleaned_num if len(cleaned_num) == 11 and cleaned_num[0] == "0"  else "Not a phone number"