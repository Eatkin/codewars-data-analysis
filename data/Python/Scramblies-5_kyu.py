# https://www.codewars.com/kata/55c04b4cc56a697bb0000048
# 2023-05-24T18:24:05.817+0000
from collections import Counter

def scramble(s1, s2):
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    
    for char, count in s2_counter.items():
        if s1_counter[char] < count:
            return False
        
    return True