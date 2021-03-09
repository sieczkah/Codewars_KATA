"""https://www.codewars.com/kata/577b9960df78c19bca00007e/train/python"""

def find_digit(num, nth):
    if len(str(num)) < nth:
        return 0
    elif nth <= 0:
        return -1
    else:
        return int(str(num)[-nth]) 
