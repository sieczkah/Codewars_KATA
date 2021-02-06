"""https://www.codewars.com/kata/5254ca2719453dcc0b00027d"""
import itertools
def permutations(string):
    perms = []
    for i in list(map(list, itertools.permutations(string, len(string)))):
        perms.append(''.join(i))
    
    return list(set(perms))
