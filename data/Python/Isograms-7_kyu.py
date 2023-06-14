# https://www.codewars.com/kata/54ba84be607a92aa900000f1
# 2023-05-24T18:15:13.706+0000
def is_isogram(string):
    return len(string) == len(set(string.lower()))