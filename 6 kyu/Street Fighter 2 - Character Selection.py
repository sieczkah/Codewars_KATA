"""https://www.codewars.com/kata/5853213063adbd1b9b0000be/train/python"""


dir_x = {'right': 1, 'left': -1}
dir_y = {'up': 0, 'down': 1}

def street_fighter_selection(fighters, initial_position, moves):
    x, y = initial_position
    char = []
    for i in moves:
        if i in dir_x.keys():
            x += dir_x[i]
        else:
            y = dir_y[i]
        char.append(fighters[y][x % 6])
    return char
