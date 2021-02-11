"""https://www.codewars.com/kata/52a382ee44408cea2500074c/solutions/python/me/best_practice"""


# returns minor matrix
def minor_matrix(matrix, cols, rows):
    return [row[:cols] + row[cols + 1:] for row in matrix[:rows] + matrix[rows + 1:]]


# counts matrix deter using laplace extension
def determinant(matrix):
    col, row = len(matrix[0]), len(matrix)
    det = 0
    sign = 1
    if col == 1:
        det += float(matrix[0][0])
        return det
    else:
        for i in range(col):
            det += float(matrix[0][i]) * sign * \
                   determinant(minor_matrix(matrix, i, 0))
            sign *= -1
        return det
