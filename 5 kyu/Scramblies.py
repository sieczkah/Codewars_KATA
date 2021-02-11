"""https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python"""

def scramble(s1, s2):
    return all(s1.count(i) - s2.count(i) >= 0 for i in set(s2))
