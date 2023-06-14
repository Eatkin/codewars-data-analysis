# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
# 2023-05-25T07:28:47.760+0000
def solution(args):
    stack = []
    prev = None
    formatted_range = []
    for num in args:
        if stack == []:
            stack.append(num)
            prev = num
            continue
            
        if num == prev + 1:
            stack.append(num)
        else:
            # Collapse the stack
            if len(stack) == 1:
                formatted_range.append(str(stack[0]))
            elif len(stack) == 2:
                formatted_range.append(str(stack[0]))
                formatted_range.append(str(stack[1]))
            else:
                formatted_range.append(str(stack[0]) + "-" + str(stack[-1]))
            stack = []
            stack.append(num)
        prev = num
    
    # Collapse the stack for the final time
    if len(stack) == 1:
        formatted_range.append(str(stack[0]))
    elif len(stack) == 2:
        formatted_range.append(str(stack[0]))
        formatted_range.append(str(stack[1]))
    else:
        formatted_range.append(str(stack[0]) + "-" + str(stack[-1]))
    
    return ",".join(formatted_range)
       
                