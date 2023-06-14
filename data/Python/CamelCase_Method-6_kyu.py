# https://www.codewars.com/kata/587731fda577b3d1b0001196
# 2023-05-24T16:12:37.689+0000
def camel_case(s):
    return "".join(word.title() for word in s.split())