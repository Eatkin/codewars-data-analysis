# https://www.codewars.com/kata/5c511d8877c0070e2c195faf
2023-05-08T17:56:43.393+0000
import math;
def validate(username, password):
    print(username, password)
    for s1, s2 in [(username, password), (password, username)]:
        substr_length = min(len(s1), math.ceil(len(s1) / 2))
        if any(s1[i:i + substr_length] in s2 for i in range(len(s1) // 2 + 1)):
            return False
        
    return True