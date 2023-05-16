# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
# 2023-04-18T18:14:46.423+0000
def duplicate_encode(word):
    word = word.lower()
    dict = {}
    for char in word:
        if char in dict:
            continue
        if word.count(char) > 1:
            dict[char] = ")"
        else:
            dict[char] = "("
            
    trans = str.maketrans(dict)
    return word.translate(trans)