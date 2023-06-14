# https://www.codewars.com/kata/59cfc000aeb2844d16000075
# 2023-05-22T09:43:46.330+0000
def capitalize(s):
    return ["".join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(s)]), "".join([char.upper() if i % 2 == 1 else char.lower() for i, char in enumerate(s)])]