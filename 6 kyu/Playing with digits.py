"""https://www.codewars.com/kata/5552101f47fc5178b1000050"""
def dig_pow(n, p):
    x = 0
    for i in range(len(str(n))):
        x += int(str(n)[i]) ** (p+i)
    k = x // n
    return k if k * n == x else -1
