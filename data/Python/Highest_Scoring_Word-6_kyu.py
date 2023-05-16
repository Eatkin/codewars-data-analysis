# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272
2023-05-12T12:51:36.097+0000
def high(x):
    return sorted(x.split(), key = lambda w: sum([ord(c) - 96 for c in w]), reverse = True)[0]