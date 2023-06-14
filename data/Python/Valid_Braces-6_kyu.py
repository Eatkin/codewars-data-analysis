# https://www.codewars.com/kata/5277c8a221e209d3f6000b56
# 2023-05-24T18:09:31.293+0000
def valid_braces(string):
    stack = ""
    opening_braces = ["(", "[", "{"]
    closing_braces = [")", "]", "}"]

    # Now we need to make sure every closing brace matches the final element on the stack
    for char in string:
        # If the stack is empty make sure we find opening braces
        if stack == "":
            if char in opening_braces:
                stack = char
            else:
                return False
        else:
            # Either add a character to the stack or try and remove it
            if char in opening_braces:
                stack += char
            else:
                if opening_braces.index(stack[-1]) == closing_braces.index(char):
                    stack = stack[:-1]
                else:
                    return False
                
    if stack == "":
        return True
    
    return False