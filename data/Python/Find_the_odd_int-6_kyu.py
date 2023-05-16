# https://www.codewars.com/kata/54da5a58ea159efa38000836
# 2023-04-18T18:19:17.774+0000
from collections import Counter
def find_it(seq):
    dict = Counter(seq)
    for num, occurences in dict.items():
        if occurences%2 != 0:
            return num