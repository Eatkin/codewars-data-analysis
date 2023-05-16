# https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08
2023-04-18T17:12:12.110+0000
def multiplication_table(size):
    table = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append((i + 1) * (j + 1))
        table.append(row)
            
    return table
        