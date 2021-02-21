"""https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python"""


def move_zeros(array):
    moved_arr = [i for i in array if i != 0 or type(i) == bool]
    return moved_arr + [0] * (len(array) - len(moved_arr))
