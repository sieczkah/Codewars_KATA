"""https://www.codewars.com/kata/5878520d52628a092f0002d0"""


def string_transformer(s):
    return ' '.join(s.swapcase().split(' ')[::-1])
