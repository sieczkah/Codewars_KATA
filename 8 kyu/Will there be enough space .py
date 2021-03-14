"""https://www.codewars.com/kata/5875b200d520904a04000003"""

def enough(cap, on, wait):
    space = cap - on - wait
    return 0 if space >= 0 else -space
