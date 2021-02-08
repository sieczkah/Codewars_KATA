"""https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python"""

def valid_parentheses(string):
    p_stack = []
    for i in string:
        if i in '()':
            if not p_stack:
                p_stack.append(i)
            else:
                if p_stack[-1] == '(' and i == ')':
                    p_stack.pop()
                else:
                    p_stack.append(i)
    return not len(p_stack)