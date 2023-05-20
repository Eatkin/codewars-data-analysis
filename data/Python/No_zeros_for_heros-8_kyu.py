# https://www.codewars.com/kata/570a6a46455d08ff8d001002
# 2023-05-17T05:44:35.292+0000
def no_boring_zeros(n):
    try:
        return int(str(n).rstrip("0"))
    except:
        return 0