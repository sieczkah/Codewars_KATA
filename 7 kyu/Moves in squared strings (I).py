"""https://www.codewars.com/kata/56dbe0e313c2f63be4000b25/train/python"""


def vert_mirror(s):
    return '\n'.join([i[::-1] for i in s.split('\n')])
def hor_mirror(s):
    return '\n'.join(s.split('\n')[::-1])
def oper(fct, s):
    return fct(s)
