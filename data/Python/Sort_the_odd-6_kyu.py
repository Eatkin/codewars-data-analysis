# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d
# 2023-05-22T09:52:18.550+0000
def sort_array(source_array):
    # Extract odds
    odds = [num for num in source_array if num%2 == 1]
    odds.sort()
    # Put them back in
    odd_index = 0
    for i, num in enumerate(source_array):
        if num%2 == 1:
            source_array[i] = odds[odd_index]
            odd_index += 1
            
    return source_array