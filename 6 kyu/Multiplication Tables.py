"""https://www.codewars.com/kata/5432fd1c913a65b28f000342"""

def multiplication_table(row,col):
    table = []
    for r in range(1, row + 1):
        table.append([i * r for i in range(1, col + 1)])
    return table
