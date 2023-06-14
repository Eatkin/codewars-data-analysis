# https://www.codewars.com/kata/5848cd33c3689be0dc00175c
# 2023-05-24T12:53:59.016+0000
def add(s1, s2):
    return sum(ord(char) for char in s1) + sum(ord(char) for char in s2)