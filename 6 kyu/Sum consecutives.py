"""https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/python"""

def sum_consecutives(s):
    products = []
    stack = [s[0]]
    for i in s[1:]:
        if stack and i == stack[-1]:
            stack.append(i)
        else:
            products.append(sum(stack))
            stack = [i]
    products.append(sum(stack))
    return products
