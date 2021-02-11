"""https://www.codewars.com/kata/569651a2d6a620b72e000059/train/python"""


options = {
    'spock': ['scissor', 'rock'],
    'scissor': ['paper', 'lizard'],
    'paper': ['rock', 'spock'],
    'rock': ['lizard', 'scissor'],
    'lizard': ['spock', 'paper']
}


def result(p1, p2):
    if p1.lower() not in options.keys() or p2.lower() not in options.keys():
        return 'Oh, Unknown Thing'
    elif p1.lower() == p2.lower().lower():
        return 'Draw!'
    else:
        return 'Player 1 won!' if p2.lower() in options[p1.lower()] else 'Player 2 won!'

