# https://www.codewars.com/kata/634913db7611b9003dff49ad
2023-05-08T12:53:50.397+0000
import re
def purify(s: str) -> str:
    return re.sub(r" {2,}", " ", re.sub(r"\w[iI]+\w|[iI]+\w|\w[iI]+|[iI]+", "", s).strip())