# https://www.codewars.com/kata/5641275f07335295f10000d0
# 2023-03-07T19:16:11.237+0000
def split_the_bill(x):
    # Code Away!
    bill_split = sum(x.values()) / len(x)
    return {friend: round(x[friend] - bill_split, 2) for friend in x}