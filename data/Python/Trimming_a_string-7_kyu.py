# https://www.codewars.com/kata/563fb342f47611dae800003c
# 2023-06-01T11:58:16.270+0000
def trim(phrase, size):
    if len(phrase) <= 3 or size <= 3:
        if len(phrase) <= size:
            return phrase
        return phrase[:size] + "..."
    return phrase[:size - 3] + "..." if len(phrase) > size else phrase