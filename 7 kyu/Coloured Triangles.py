"""https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/python"""


def colProd(col1, col2):
    colour = [i for i in 'RGB' if i not in (col1, col2)]
    return col1 if col1 == col2 else colour[0]

def triangle(row):
    if len(row) == 1:
        return row
    else:
        lower_row = ''.join(colProd(row[i], row[i + 1]) for i in range(len(row) - 1))
        return triangle(lower_row)

