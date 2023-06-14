# https://www.codewars.com/kata/51b6249c4612257ac0000005
# 2023-05-31T14:05:35.848+0000
ROMAN_DICT = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
def solution(roman):
    value = 0
    for i, c in enumerate(roman):
        try:
            if ROMAN_DICT[c] < ROMAN_DICT[roman[i + 1]]:
                value -= ROMAN_DICT[c]
                continue
            value += ROMAN_DICT[c]
        except:
            value += ROMAN_DICT[c]
            
    return value