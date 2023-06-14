# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
# 2023-06-02T14:03:02.766+0000
import numpy as np
def validate_battlefield(field):
    # keys are size of ship, values are length
    SHIP_DICT = {
        4: 1,
        3: 2,
        2: 3,
        1: 4
    }

    ships_found = 0
    field = np.array(field) # For easier slicing
    # Let's start iterating over the array
    for i in range(100):
        row = i // 10
        column = i % 10
        # We've found what could be a ship - let's begin our search
        # Since we go top left to bottom right, the ship can only be down or to the right
        if field[row, column] == 1:
            # Edge case 1: ship to the bottom left diagonally
            if row < 9 and column > 0 and field[row + 1, column - 1] == 1:
                return False
            field[row, column] = 0
            size = 1
            orientation = ""
            # Check column-wise
            i = 1
            while column + i < 10 and field[row, column + i] == 1:
                field[row, column + i] = 0
                size += 1
                orientation = "h"
                i += 1
            # Check row-wise if we haven't already found a ship
            if orientation == "":
                i = 1
                while row + i < 10 and field[row + i, column] == 1:
                    field[row + i, column] = 0
                    size += 1
                    orientation = "v"
                    i += 1
                    
            # Edge case 2: ship to the bottom right diagonally
            rr, cc = row, column
            if orientation == "v":
                rr += size
                cc += 1
            else:
                rr += 1
                cc += size
            
            if rr < 10 and cc < 10:
                if field[rr, cc] == 1:
                    return False
            
            # Now we've found a ship, we can verify it
            if size < 5:
                SHIP_DICT[size] -= 1
                if SHIP_DICT[size] < 0:
                    print("Too many ships", row, column)
                    return False
            else:
                print("Ship too big", row, column)
                return False
            
            # Now we can check to the immediate right/below to make sure there's not any conflicts
            if orientation == "v" and column < 9:
                for i in range(size):
                    if field[row + i, column + 1] == 1:
                        print("Ship found adjacent to vertical ship", row, column)
                        return False
                    
            if orientation == "h" and row < 9:
                for i in range(size):
                    if field[row + 1, column] == 1:
                        print("Ship found adjacent to horizontal ship", row, column)
                        return False
                    
    # Verify all dictionary values are 0
    for value in SHIP_DICT.values():
        if value != 0:
            print("Not enough ships found")
            return False
                
                
            
    return True