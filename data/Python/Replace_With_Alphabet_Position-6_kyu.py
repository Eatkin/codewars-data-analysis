# https://www.codewars.com/kata/546f922b54af40e1e90001da
# 2023-05-07T08:05:42.084+0000
def alphabet_position(text):
    return " ".join([str(ord(letter.lower()) - 96) for word in text.split() for letter in word if letter.isalpha()])