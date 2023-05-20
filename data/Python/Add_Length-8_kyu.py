# https://www.codewars.com/kata/559d2284b5bb6799e9000047
# 2023-05-19T20:44:01.549+0000
def add_length(str_):
    return [f"{s} {len(s)}" for s in str_.split()]