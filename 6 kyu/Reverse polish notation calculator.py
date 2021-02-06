"""https://www.codewars.com/kata/52f78966747862fc9a0009ae"""
import operator
OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def calc(expr):
    expr = expr.split()
    stack = []
    if not expr:
        return 0
    for i in expr:
        if i in OPERATORS.keys():
            a, b = stack.pop(-1), stack.pop(-1)
            stack.append(OPERATORS[i](b,a))
        else:
            stack.append(float(i))
    return stack.pop()
