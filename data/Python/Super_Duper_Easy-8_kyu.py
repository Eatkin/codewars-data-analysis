# https://www.codewars.com/kata/55a5bfaa756cfede78000026
2023-05-12T14:33:52.041+0000
def problem(a):
    try:
        return (a * (1 * 2 * 3 * 4 * 5 - 20)) / 2 + 3 ** 2 -3
    except TypeError:
        print("You absolute doofus, you didn't supply a number, what were you thinking?")
        return "Error"