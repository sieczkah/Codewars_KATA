"""https://www.codewars.com/kata/57a6633153ba33189e000074/train/python"""

def ordered_count(inp):
    used = []
    letters = []
    for l in inp:
        if l not in used:
            letters.append((l, inp.count(l)))
            used.append(l)
    return letters
