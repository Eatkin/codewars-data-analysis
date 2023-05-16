# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e
# 2023-05-11T13:42:38.920+0000
def expression_matter(a, b, c):
    # Find the largest combination of a, b and c
    combos = [a + b + c,
              a * b * c,
              a + (b * c),
              (a + b) * c,
              a * (b + c),
              (a * b) + c]
    return max(combos)