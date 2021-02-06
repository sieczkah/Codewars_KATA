"""https://www.codewars.com/kata/5672682212c8ecf83e000050"""
def dbl_linear(n):
    dbl = [1]
    x = 0
    y = 0
    while len(dbl) <= n:
        a = dbl[x] * 2 + 1
        b = dbl[y] * 3 + 1
        if a < b:
            dbl.append(a)
            x += 1
        elif a == b:
            dbl.append(a)
            x += 1
            y += 1
        else:
            dbl.append(b)
            y += 1
    return dbl[n]
