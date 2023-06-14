# https://www.codewars.com/kata/52b757663a95b11b3d00062d
# 2023-06-06T08:40:05.639+0000
def to_weird_case(words):
    words = words.split()
    for i, word in enumerate(words):
        words[i] = "".join([letter.upper() if j % 2 == 0 else letter.lower() for j, letter in enumerate(word)])
    return " ".join(words)