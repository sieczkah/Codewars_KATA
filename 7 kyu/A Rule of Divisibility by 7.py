"""https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/python"""

def seven(m, steps=0):
    while m > 99:
        steps += 1
        m = int(str(m)[:-1]) - int(str(m)[-1])*2 
    return (m, steps)
