"""https://www.codewars.com/kata/586dd26a69b6fd46dd0000c0"""

def my_first_interpreter(code):
    cell = 0
    msg = ''
    for i in code:
        if cell == 256: cell = 0
        if i == '+':
            cell += 1
        elif i == '.':
            msg += chr(cell)
    return msg
