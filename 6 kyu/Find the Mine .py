"""https://www.codewars.com/kata/528d9adf0e03778b9e00067e"""

def mineLocation(field):
    for ind, row in enumerate(field):
        if 1 in row:
            row_i = ind
            col_i = row.index(1)
    return [row_i, col_i]
    
