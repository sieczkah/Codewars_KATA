"""https://www.codewars.com/kata/57cf50a7eca2603de0000090"""

from string import ascii_lowercase as let
def move_ten(st):
    return ''.join(let[(let.find(i) + 10) % len(let)] for i in st)
