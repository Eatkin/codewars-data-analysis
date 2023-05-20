# https://www.codewars.com/kata/5769b3802ae6f8e4890009d2
# 2023-05-17T05:46:40.302+0000
def remove_every_other(my_list):
    return [element for i, element in enumerate(my_list) if i%2 == 0 or i == 0]