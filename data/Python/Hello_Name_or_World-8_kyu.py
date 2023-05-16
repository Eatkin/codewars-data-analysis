# https://www.codewars.com/kata/57e3f79c9cb119374600046b
# 2023-04-17T18:04:02.137+0000
def hello(name=""):
    return f"Hello, {name[0].upper() + name[1:].lower()}!" if name else "Hello, World!"