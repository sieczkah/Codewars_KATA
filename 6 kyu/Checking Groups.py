"""https://www.codewars.com/kata/54b80308488cb6cd31000161"""

def group_check(s):
    pairs = {'{': '}', '(': ')', '[': ']'}
    p_stack = []
    for par in s:
        if p_stack and p_stack[-1] in pairs.keys():
            if par == pairs[p_stack[-1]]:
                p_stack.pop()
            else:
                p_stack.append(par)
        else:
            p_stack.append(par)
    return len(p_stack) == 0
