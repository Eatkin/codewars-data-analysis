# https://www.codewars.com/kata/5263c6999e0f40dee200059d
# 2023-05-31T14:21:18.919+0000
PIN_DICT = {
    "1": ["1", "2", "4"],
    "2": ["1", "2", "3", "5"],
    "3": ["2", "3", "6"],
    "4": ["1", "4", "5", "7"],
    "5": ["2", "4", "5", "6", "8"],
    "6": ["3", "5", "6", "9"],
    "7": ["4", "7", "8"],
    "8": ["5", "7", "8", "9", "0"],
    "9": ["6", "8", "9"],
    "0": ["8", "0"]
}
def get_pins(observed):
    possible_pins = []
    # A depth search would be a good idea here
    if len(observed) > 1:
        pins = get_pins(observed[1:])
        for num in PIN_DICT[observed[0]]:
            for pin in pins:
                possible_pins.append(num + pin)
    else:
        return PIN_DICT[observed]
    
    return possible_pins    