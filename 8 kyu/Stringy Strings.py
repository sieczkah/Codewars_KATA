"""https://www.codewars.com/kata/563b74ddd19a3ad462000054/train/python"""


def stringy(size):
    return ''.join([str(i % 2) for i in range(1,size + 1)])
