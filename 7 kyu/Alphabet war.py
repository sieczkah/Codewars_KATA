"""https://www.codewars.com/kata/59377c53e66267c8f6000027/python"""

l_side = {'w': 4, 'p': 3, 'b': 2, 's': 1}
r_side = {'m': 4, 'q': 3, 'd': 2, 'z': 1}

def alphabet_war(fight):
    l_string = sum(l_side[i] for i in fight if i in 'wpbs')
    r_string = sum(r_side[i] for i in fight if i in 'mqdz')
    if l_string == r_string:
        return "Let's fight again!"
    else:
        return "Right side wins!" if r_string > l_string else "Left side wins!"
