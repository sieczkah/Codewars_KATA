"""https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/python"""


from math import ceil

def declare_winner(fighter1, fighter2, first_attacker):
    # countig moves needed to bring opponents health to 0
    f1_moves = ceil(fighter2.health / fighter1.damage_per_attack)
    f2_moves = ceil(fighter1.health / fighter2.damage_per_attack)
    # if needed moves are the same first_attacker wins
    if f1_moves == f2_moves:
        return first_attacker
    elif f1_moves < f2_moves:
        return fighter1.name
    else:
        return fighter2.name
