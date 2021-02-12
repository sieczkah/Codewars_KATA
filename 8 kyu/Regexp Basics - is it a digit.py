"""https://www.codewars.com/kata/567bf4f7ee34510f69000032/train/python"""


import re


def is_digit(n):
    return bool(re.match(r'^\d+$', n))
