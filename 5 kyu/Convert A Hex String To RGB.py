"""https://www.codewars.com/kata/5282b48bb70058e4c4000fa7"""

from textwrap import wrap
def hex_string_to_RGB(hex_string): 
    return {col: int(val, 16) for col,val in zip(['r','g','b'], wrap(hex_string[1:], 2))}
