# https://www.codewars.com/kata/57f24e6a18e9fad8eb000296
# 2023-05-20T08:24:35.792+0000
def how_much_i_love_you(nb_petals):
    love_dict = {
        0: "I love you",
        1: "a little",
        2: "a lot",
        3: "passionately",
        4: "madly",
        5: "not at all"
    }
    return love_dict[(nb_petals - 1) % 6]