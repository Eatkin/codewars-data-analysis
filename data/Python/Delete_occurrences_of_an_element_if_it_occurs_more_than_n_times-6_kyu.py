# https://www.codewars.com/kata/554ca54ffa7d91b236000023
# 2023-03-08T11:33:54.167+0000
def delete_nth(order,max_e):
    return [num for index, num in enumerate(order) if order[:index].count(num) < max_e]