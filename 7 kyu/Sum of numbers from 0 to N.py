"""https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763/train/python"""


def show_sequence(n):
    if n < 0:
        return f'{n}<0'
    elif n == 0:
        return '0=0'
    else:
        lst = list(range(n+1))
        return f"{'+'.join(map(str, lst))} = {sum(lst)}"

