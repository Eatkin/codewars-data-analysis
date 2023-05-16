# https://www.codewars.com/kata/5412509bd436bd33920011bc
2023-03-07T19:24:39.991+0000
# return masked string
def maskify(cc):
    return "#" * max(0, (len(cc) - 4)) + cc[-4:]