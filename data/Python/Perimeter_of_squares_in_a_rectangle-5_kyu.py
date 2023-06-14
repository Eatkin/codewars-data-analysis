# https://www.codewars.com/kata/559a28007caad2ac4e000083
# 2023-05-25T17:41:24.926+0000
fib_cache = {
        0: 1,
        1: 1
    }

def generate_fibs(n):
    for i in range(n):
        if i not in fib_cache:
            fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]
    
def fib(n):
    try:
        return fib_cache[n]
    except:
        fib_cache[n] = fib(n-1) + fib(n-2)
        return fib_cache[n]

def perimeter(n):
    generate_fibs(n)
    return 4 * (fib(n + 2) - 1)