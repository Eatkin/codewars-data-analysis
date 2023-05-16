# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
2023-03-08T17:29:14.345+0000
def snail(snail_map):
    #This solution sucks, sorry
    array_size = len(snail_map)
    if len(snail_map[0]) == 0:
        return []
    turns = 3
    steps = array_size - 1
    hmove = True
    vmove = False
    hdir = 1   
    vdir = -1  # Must start at -1 ince it gets flipepd at the first turn     
    row = 0
    column = 0
    snail_array = list()
    while len(snail_array) < array_size ** 2:
        for i in range(turns):
            for j in range(steps):
                snail_array.append(snail_map[row][column])
                column += hmove * hdir
                row += vmove * vdir
                
            hmove = not hmove
            vmove = not vmove
            if hmove:
                hdir *= -1
            if vmove:
                vdir *= -1
            
        turns = max(turns - 1, 2)
        steps = max(steps - 1, 1)
        
    # I made a mistake so there's one extra value on the end lol
    return snail_array[:-1]