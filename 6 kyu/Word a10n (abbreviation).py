"""https://www.codewars.com/kata/5375f921003bf62192000746/train/python"""


import re


def abbreviate(s):
    word_sign = re.findall(r'[A-Za-z]+|\W|\d|_', s)
    a10n = [w if len(w) < 4 else w[0] + str(len(w) - 2) + w[-1]
            for w in word_sign]
    return ''.join(a10n)
