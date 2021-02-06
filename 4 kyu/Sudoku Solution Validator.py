"""https://www.codewars.com/kata/529bf0e9bdf7657179000008"""
def valid_solution(board):
    lista = []
    for i in board:
        lista += i
        if len(set(i)) != 9:
            return False
    if lista.count(0) > 1:
        return False
    for i in range(9):
        row = []
        for x in range(9):
            row.append(board[x][i])
        if len(set(row)) != 9:
            return False
    for i in (3, 6, 9):
        small_sqr = []
        for x in (3, 6, 9):
            small_sqr = board[x-3][i-3:i] + board[x-2][i-3:i] + board[x-1][i-3:i]
            # print(small_sqr)
        if len(set(small_sqr)) != 9:
            return False
    return True
