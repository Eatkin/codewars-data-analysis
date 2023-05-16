# https://www.codewars.com/kata/5637b03c6be7e01d99000046
2023-04-18T17:00:08.170+0000
def make_password(phrase):
    words = phrase.split()
    password = "".join([letter[0] for letter in words])
    translation = str.maketrans("iIoOsS", "110055")
    return password.translate(translation)