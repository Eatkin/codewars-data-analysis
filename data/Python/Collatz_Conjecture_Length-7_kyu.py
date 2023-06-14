# https://www.codewars.com/kata/54fb963d3fe32351f2000102
# 2023-05-23T06:06:38.704+0000
def collatz(n):
    iters = 1
    while n != 1:
        n = n//2 if n%2 == 0 else n * 3 + 1
        iters += 1
        
    return iters