# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
2023-05-11T13:45:48.417+0000
def accum(s):
    output_list = []
    for i, char in enumerate(s):
        output_list.append((char * (i + 1)).capitalize())
    
    return "-".join(output_list)