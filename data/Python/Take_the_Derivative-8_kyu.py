# https://www.codewars.com/kata/5963c18ecb97be020b0000a2
# 2023-05-22T10:00:45.104+0000
def derive(coefficient, exponent): 
    return "".join([str(coefficient * exponent), "x^", str(exponent - 1)])