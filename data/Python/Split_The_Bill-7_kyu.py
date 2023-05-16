# https://www.codewars.com/kata/5641275f07335295f10000d0
2023-03-07T19:15:07.662+0000
def split_the_bill(x):
    # Code Away!
    bill_total = sum(x.values())
    bill_split = bill_total / len(x)
    x = {friend: round(x[friend] - bill_split, 2) for friend in x}
    return x