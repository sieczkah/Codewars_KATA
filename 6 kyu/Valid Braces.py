"""https://www.codewars.com/kata/5277c8a221e209d3f6000b56"""

pairs = {'{': '}', '(': ')', '[': ']'}
def validBraces(string):
    p_stack = []
    for par in string:
        if p_stack and p_stack[-1] in pairs.keys():
            if par == pairs[p_stack[-1]]:
                p_stack.pop()
            else:
                p_stack.append(par)
        else:
            p_stack.append(par)
    return len(p_stack) == 0

