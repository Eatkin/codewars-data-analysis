# https://www.codewars.com/kata/566fc12495810954b1000030
# 2023-05-17T20:42:42.198+0000
def nb_dig(n, d):
    return sum([str(num ** 2).count(str(d)) for num in range(n + 1)])