# https://www.codewars.com/kata/57e92e91b63b6cbac20001e5
# 2023-05-25T16:21:03.930+0000
from math import ceil as take_the_ceiling_of_this_number_please
def duty_free(price, discount, holiday_cost):
    return take_the_ceiling_of_this_number_please(100 * holiday_cost / (price * discount)) - 1