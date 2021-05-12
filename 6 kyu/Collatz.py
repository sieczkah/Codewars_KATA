"""https://www.codewars.com/kata/5286b2e162056fd0cb000c20"""

def collatz(n):
    prod = []
    while True:
        prod.append(n)
        if n == 1:
            break
        elif n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    return '->'.join(map(str, prod))
