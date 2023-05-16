# https://www.codewars.com/kata/5b817c2a0ce070ace8002be0
# 2023-04-22T13:49:49.588+0000
def display_board(board, width):
    cells = len(board) + 1
    # Shouldn't get an irregular shaped board but just in case
    height = cells // width
    ascii_board = ""
    
    for i in range(height):
        for j in range(width):
            ascii_board += f" {board[i * width + j]} "
            if j < width - 1:
                ascii_board += "|"
        if i < height - 1:
            # Print the correct number of dashes
            ascii_board += "\n" + "-" * (width * 4 - 1) + "\n"
            
    return ascii_board