# https://www.codewars.com/kata/568d0dd208ee69389d000016
2023-05-07T08:31:27.002+0000
def rental_car_cost(d):
    return d * 40 if d < 3 else (d * 40 - 50 if d >= 7 else d * 40 - 20)