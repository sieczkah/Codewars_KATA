"""https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python"""


def clean_string(s):
    stack = []
    for i in s:
        if i == '#' and len(stack) > 0:
            stack.pop()
        elif i != '#':
            stack.append(i)
    return ''.join(stack)
