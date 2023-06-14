# https://www.codewars.com/kata/5bb0c58f484fcd170700063d
# 2023-05-23T07:09:39.483+0000
def pillars(num_pill, dist, width):
    return (num_pill - 1) * dist * 100 + max(0, (num_pill - 2)) * width