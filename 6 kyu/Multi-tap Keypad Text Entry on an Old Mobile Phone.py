"""https://www.codewars.com/kata/54a2e93b22d236498400134b"""

keyboard = ['1', 'ABC2', 'DEF3',
            'GHI4', 'JKL5', 'MNO6',
            'PQRS7', 'TUV8', 'WXYZ9',
            '*', ' 0', '#']


def presses(phrase):
    clicks = 0
    for letter in phrase.upper():
        for button in keyboard:
            if letter in button:
                clicks += button.find(letter) + 1
    return clicks
