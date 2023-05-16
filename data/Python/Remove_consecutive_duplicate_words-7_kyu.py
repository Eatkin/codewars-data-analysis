# https://www.codewars.com/kata/5b39e91ee7a2c103300018b3
# 2023-05-05T14:03:34.261+0000
import re
def remove_consecutive_duplicates(s : str) -> str:
    return " ".join(re.findall(r"\b(\S+)\b(?! \b\1\b)", s))