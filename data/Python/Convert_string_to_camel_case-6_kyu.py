# https://www.codewars.com/kata/517abf86da9663f1d2000003
2023-04-29T12:17:55.855+0000
import re

def to_camel_case(text):
    regex = r'[^\w]+'
    words = "_".join(re.split(regex, text))
    words = re.split(r'_+', words)
    return "".join([word.capitalize() if i > 0 else word for i, word in enumerate(words)])