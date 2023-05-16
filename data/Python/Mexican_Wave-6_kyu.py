# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029
# 2023-04-18T17:09:01.181+0000
def wave(people):
    if len(people) == 0:
        return []
    wave = []
    
    for i in range(0, len(people)):
        if people[i] == " ":
            continue
        wave.append(people[:i] + people[i].upper() + people[i+1:])
    
    return wave