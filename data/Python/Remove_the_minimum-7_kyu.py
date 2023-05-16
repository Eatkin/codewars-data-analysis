# https://www.codewars.com/kata/563cf89eb4747c5fb100001b
2023-05-14T06:39:08.191+0000
def remove_smallest(numbers):
    if numbers:
        poop = numbers.copy()
        poop.pop(poop.index(min(poop)))
    return numbers if not numbers else poop