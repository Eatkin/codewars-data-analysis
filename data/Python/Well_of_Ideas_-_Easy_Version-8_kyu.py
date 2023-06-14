# https://www.codewars.com/kata/57f222ce69e09c3630000212
# 2023-05-24T16:14:05.181+0000
def well(x):
    goods = x.count("good")
    return "Fail!" if goods == 0 else "Publish!" if goods <= 2 else "I smell a series!"