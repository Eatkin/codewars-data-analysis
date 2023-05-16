# https://www.codewars.com/kata/530e15517bc88ac656000716
2023-05-13T14:49:14.038+0000
def rot13(message):
    return message.translate(str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))