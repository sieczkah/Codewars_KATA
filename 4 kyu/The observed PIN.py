"""https://www.codewars.com/kata/5263c6999e0f40dee200059d"""


import itertools
def get_pins(observed):
    possible_comb = {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '6', '5', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['8', '0'],
    }
    near_numb = [possible_comb[i] for i in observed]
    return [''.join(n) for n in list(itertools.product(*near_numb))]
