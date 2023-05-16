# https://www.codewars.com/kata/55c45be3b2079eccff00010f
2023-05-06T12:32:20.551+0000
import re
def order(sentence):
    return "" if not sentence else " ".join(sorted(sentence.split(), key = lambda word: re.findall(r"\d", word)))