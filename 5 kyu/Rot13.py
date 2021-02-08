"""https://www.codewars.com/kata/530e15517bc88ac656000716/train/python"""

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rot13(message):
    msg = ''
    for i in message:
        if i in lower:
            msg += lower[(lower.find(i) + 13) % len(lower)]
        elif i in upper:
            msg += upper[(upper.find(i) + 13) % len(upper)]
        else:
            msg += i
    return ''.join(msg)
