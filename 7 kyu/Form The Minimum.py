"""https://www.codewars.com/kata/5ac6932b2f317b96980000ca/solutions/python/me/best_practice"""

def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))
