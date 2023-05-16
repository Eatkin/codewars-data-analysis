# https://www.codewars.com/kata/55968ab32cf633c3f8000008
# 2023-05-05T13:34:26.466+0000
import re
def initials(name):
    name_components = re.findall(r"(\w)\w+\b(?!$)|(\w+)$", name)
    return ".".join([word[0].capitalize() if word[0] else word[1].capitalize() for word in name_components])