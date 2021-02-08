"""https://www.codewars.com/kata/5b180e9fedaa564a7000009a/solutions/python/me/best_practice"""

def solve(s):
    prod = [1 if i.islower() else 0 for i in s]
    return s.upper() if sum(prod) < (len(prod) // 2) else s.lower()
