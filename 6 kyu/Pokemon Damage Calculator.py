"""https://www.codewars.com/kata/536e9a7973130a06eb000e9f"""

def set_bonus(my_type, opp_type):
    neutral = {'fire':'electric', 'grass': 'electric'}
    bonus = {'fire': 'grass', 'water': 'fire', 'grass': 'water', 'electric': 'water'}
    if neutral.get(my_type, None) == opp_type or neutral.get(opp_type, None) == my_type:
        return 1
    elif bonus[my_type] == opp_type:
        return 2
    else:
        return 0.5

def calculate_damage(your_type, opponent_type, attack, defense):
    bonus = set_bonus(your_type, opponent_type)
    return 50 * (attack / defense) * bonus
