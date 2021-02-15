"""https://www.codewars.com/kata/5aa736a455f906981800360d/train/python"""


def feast(beast, dish):
    return all([beast[0] == dish[0], beast[-1] == dish[-1]])
