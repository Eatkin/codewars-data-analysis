# https://www.codewars.com/kata/59706036f6e5d1e22d000016
# 2023-05-20T08:25:59.868+0000
def words_to_marks(s):
    return sum(ord(char.lower()) - 96 for char in s)