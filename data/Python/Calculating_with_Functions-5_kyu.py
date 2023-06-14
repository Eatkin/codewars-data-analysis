# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
# 2023-05-23T09:53:46.400+0000
def zero(operation = None):
    if operation:
        return operation(0)
    else:
        return 0
def one(operation = None):
    if operation:
        return operation(1)
    else:
        return 1
def two(operation = None):
    if operation:
        return operation(2)
    else:
        return 2
def three(operation = None):
    if operation:
        return operation(3)
    else:
        return 3
def four(operation = None):
    if operation:
        return operation(4)
    else:
        return 4
def five(operation = None):
    if operation:
        return operation(5)
    else:
        return 5
def six(operation = None):
    if operation:
        return operation(6)
    else:
        return 6
def seven(operation = None):
    if operation:
        return operation(7)
    else:
        return 7
def eight(operation = None):
    if operation:
        return operation(8)
    else:
        return 8
def nine(operation = None):
    if operation:
        return operation(9)
    else:
        return 9

def plus(num):
    return lambda x: x + num
def minus(num):
    return lambda x: x - num
def times(num):
    return lambda x: x * num
def divided_by(num):
    return lambda x: x // num
    
