"""https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python"""


def solve(s):
    cons_subs = []
    stack = []
    for cons in s:
        if cons not in 'aeiou':
            stack.append(ord(cons) - 96)
        else:
            cons_subs.append(sum(stack))
            stack = []
    return max(cons_subs)
