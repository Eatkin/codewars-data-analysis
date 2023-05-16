# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
2023-05-07T08:43:06.153+0000
def filter_list(l):
    return list(filter(lambda x: type(x) == int, l))