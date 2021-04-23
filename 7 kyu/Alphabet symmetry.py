"""https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0"""

from string import ascii_lowercase as asc

def ocupy(word):
    return sum([1 if pos == asc.index(let) else 0 for pos, let in enumerate(word.lower())])

def solve(arr):
    return list(map(ocupy, arr))
    
