"""https://www.codewars.com/kata/557e8a141ca1f4caa70000a6"""

def is_triangle_number(number):
    if isinstance(number, (int, float)):
        # Number is triangle if 8 * n + 1 is square
        check = (8 * number + 1)** 0.5
        return check.is_integer()
    else:
        return False
