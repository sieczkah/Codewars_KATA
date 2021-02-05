"""https://www.codewars.com/kata/576757b1df89ecf5bd00073b"""


def tower_builder(n_floors):
    tower = []
    for i in range(1, n_floors):
        level = ' ' * (n_floors - i) + '*' * i + '*' * (i - 1) + ' ' * (n_floors - i)
        tower.append(level)
    tower.append('*' * (n_floors + (n_floors - 1)))
    return tower
