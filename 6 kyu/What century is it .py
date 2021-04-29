"""https://www.codewars.com/kata/52fb87703c1351ebd200081f"""

import math

def what_century(year):
    century = int(year) / 100
    if century.is_integer():
        century_str = str(int(century))
    else:
        century_str = str(math.ceil(century))
    sufixes = {'1': 'st', '2': 'nd', '3': 'rd'}
    if century_str in ['11', '12', '13']:
        return century_str + 'th'
    return century_str + sufixes.get(century_str[-1], 'th')
