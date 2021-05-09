"""https://www.codewars.com/kata/546a3fea8a3502302a000cd2"""

def find_the_ball(start, swaps):
    ball = start
    for x, y in swaps:
        if x == ball:
            ball = y
        elif y == ball:
            ball = x
    return ball
