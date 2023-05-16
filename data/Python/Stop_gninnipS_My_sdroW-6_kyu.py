# https://www.codewars.com/kata/5264d2b162488dc400000001
# 2023-04-20T17:32:28.547+0000
def spin_words(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])