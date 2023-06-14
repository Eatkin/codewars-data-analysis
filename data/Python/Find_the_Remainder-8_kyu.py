# https://www.codewars.com/kata/524f5125ad9c12894e00003f
# 2023-05-22T09:46:31.987+0000
def remainder(a,b):
    try:
        return max(a, b) % min(a, b)
    except:
        return None