# https://www.codewars.com/kata/5813d19765d81c592200001a
# 2023-05-24T04:49:32.639+0000
def dont_give_me_five(start,end):
    fives = 0
    for i in range(start, end + 1):
        if not "5" in str(i):
            fives += 1
    return fives
