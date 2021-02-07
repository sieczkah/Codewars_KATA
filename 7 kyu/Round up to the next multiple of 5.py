"""https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python"""

def round_to_next5(n):
    return n if not n % 5 else (n // 5 + 1) * 5
