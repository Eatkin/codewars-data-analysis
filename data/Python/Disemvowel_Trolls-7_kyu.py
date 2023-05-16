# https://www.codewars.com/kata/52fba66badcd10859f00097e
2023-05-05T13:17:48.415+0000
import re
def disemvowel(string_):
    return re.sub(r"[aeiou]", "", string_, flags = re.IGNORECASE)