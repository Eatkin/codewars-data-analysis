# https://www.codewars.com/kata/5763bb0af716cad8fb000580
# 2023-06-02T17:55:07.819+0000
def count_squares(cuts):
    return 1 if cuts == 0 else (cuts + 1) ** 3 - (cuts - 1) ** 3