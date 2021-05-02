"""https://www.codewars.com/kata/5511b2f550906349a70004e1"""

# last digits of big number are reccurent
# depending on last digit of number taken to power n2
# we have various possibilties of last digits
posib_digit = {0: 0, 1: 1, 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6],
               5: 5, 6: 6, 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1]}
# e.g. 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16, 2^5 = 32....

def last_digit(n1, n2):
    lst_digit = int(str(n1)[-1])
    posib = posib_digit[lst_digit]
    if n2 == 0:
        return 1
    elif isinstance(posib, int):
        return posib
    else:
        return posib[n2 % len(posib) - 1]
