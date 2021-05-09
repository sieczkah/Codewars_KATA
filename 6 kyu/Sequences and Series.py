"""https://www.codewars.com/kata/5254bd1357d59fbbe90001ec"""

def get_score(n):
    r = 50
    x = 0
    for i in range(n):
        x += r
        r += 50
    return x
