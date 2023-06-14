# https://www.codewars.com/kata/57126304cdbf63c6770012bd
# 2023-05-23T08:21:11.669+0000
def isDigit(string):
    try:
        float(string.strip())
        return True
    except:
        return False