"""https://www.codewars.com/kata/513e08acc600c94f01000001/train/python"""

def rounding(x):
    if x < 0:
        return 0
    else:
        return x if x < 255 else 255


def rgb(r, g, b):
    rgb = [rounding(i) for i in (r, g, b)]
    return ''.join(hex(i)[2:].upper().zfill(2) for i in rgb)
