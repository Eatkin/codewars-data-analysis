# https://www.codewars.com/kata/57ed30dde7728215300005fa
# 2023-06-01T11:59:32.500+0000
def bumps(road):
    if road.count("n") > 15:
        return "Car Dead"
    return "Woohoo!"