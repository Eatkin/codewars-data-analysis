# https://www.codewars.com/kata/539ee3b6757843632d00026b
2023-05-13T08:55:53.007+0000
def capitals(word):
    return [i for i, letter in enumerate(word) if letter == letter.upper()]