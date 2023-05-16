# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
2023-05-12T14:23:26.089+0000
def find_short(s):
    return len(sorted(s.split(), key = len)[0])