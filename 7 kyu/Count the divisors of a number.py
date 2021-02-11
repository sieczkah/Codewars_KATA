"""https://www.codewars.com/kata/542c0f198e077084c0000c2e/solutions/python"""


def divisors(n):
    return len([i for i in range(1, n+1) if not (n % i)])

