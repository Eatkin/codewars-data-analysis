# https://www.codewars.com/kata/5266876b8f4bf2da9b000362
2023-05-11T14:19:39.890+0000
def likes(names):
    if not names:
        return "no one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    
    return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"