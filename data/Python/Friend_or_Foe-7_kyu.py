# https://www.codewars.com/kata/55b42574ff091733d900002f
# 2023-05-22T10:02:05.199+0000
def friend(x):
    return [friend for friend in x if len(friend) == 4]