# https://www.codewars.com/kata/51e0007c1f9378fa810002a9
# 2023-06-12T10:24:40.051+0000
def parse(data):
    instructions = {
        "i": lambda x: x.__setitem__(0, x[0] + 1),
        "d": lambda x: x.__setitem__(0, x[0] - 1),
        "s": lambda x: x.__setitem__(0, x[0] ** 2),
        "o": lambda x: x.append(x[0])
    }
    bus = [0]
    for instruction in data:
        instructions.get(instruction, lambda x: None)(bus)
            
    return bus[1:]