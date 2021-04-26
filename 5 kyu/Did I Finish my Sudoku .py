"""https://www.codewars.com/kata/53db96041f1a7d32dc0004d2"""

valid_set = set(range(1, 10))

def done_or_not(board):
    for row in range(9):
        # checking rows
        if set(board[row]) != valid_set:
            return "Try again!"

        # checking colums
        columns = [board[i][row] for i in range(9)]
        if set(columns) != valid_set:
            return 'Try again!'

    # checking squares
    for i in range(0, 9, 3):
        for k in range(0, 9, 3):
            square = board[i][k: k + 3] + board[i + 1][k: k + 3] + board[i + 2][k: k + 3]
            if set(square) != valid_set:
                return 'Try again!'
    return "Finished!"
