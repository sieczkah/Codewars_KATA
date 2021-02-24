"""https://www.codewars.com/kata/57faa6ff9610ce181b000028/solutions/python/following/best_practice"""


def crap(garden, bags, cap):
    whole = ''.join(map(lambda x: ''.join(x), garden))
    if 'D' in whole:
        return 'Dog!!'
    else:
        return 'Cr@p' if whole.count('@') > bags * cap else 'Clean'
