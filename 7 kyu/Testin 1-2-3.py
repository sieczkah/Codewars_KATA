"""https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9"""


def number(lines):
    return [f'{n}: {l}' for n, l in enumerate(lines, 1)]
