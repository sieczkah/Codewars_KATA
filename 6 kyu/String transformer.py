"""https://www.codewars.com/kata/5878520d52628a092f0002d0"""

def string_transformer(s):
    return ' '.join(list(map(lambda x: x.swapcase(), s.split(' ')[::-1])))
