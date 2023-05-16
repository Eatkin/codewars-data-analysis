# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# 2023-04-18T18:10:29.528+0000
from collections import Counter
def duplicate_count(text):
    text = text.lower()
    dict = Counter(text)
    repeats = 0
    for value in dict.values():
        if value > 1:
            repeats += 1
            
    return repeats