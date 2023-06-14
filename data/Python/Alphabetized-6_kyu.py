# https://www.codewars.com/kata/5970df092ef474680a0000c9
# 2023-05-24T12:59:33.823+0000
def alphabetized(s):
    sorted_string = sorted(s, key=lambda x: (ord(x.lower()), s.index(s)))
    return "".join(char for char in sorted_string if char.isalpha())