"""https://www.codewars.com/kata/57f625992f4d53c24200070e/train/python"""

def bingo(ticket,win):
    mini_win = [ord_no for letters, ord_no in ticket if ord_no in [ord(i) for i in letters]]
    return 'Winner!' if len(mini_win) >= win else "Loser!"
