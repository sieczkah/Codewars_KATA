"""https://www.codewars.com/kata/550f22f4d758534c1100025a"""

direct = {
    'WEST': 'EAST',
    'EAST': 'WEST',
    'SOUTH': 'NORTH',
    'NORTH': 'SOUTH',
}


def dirReduc(arr):
    reduced = []
    for i in arr:
        if reduced and direct[i] == reduced[-1]:
            del reduced[-1]
        else:
            reduced.append(i)
    return reduced
