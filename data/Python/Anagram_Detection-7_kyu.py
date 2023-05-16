# https://www.codewars.com/kata/529eef7a9194e0cbc1000255
2023-05-13T14:46:20.015+0000
# write the function is_anagram
def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())