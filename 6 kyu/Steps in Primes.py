"""https://www.codewars.com/kata/5613d06cee1e7da6d5000055"""

import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and i != n:
            return False
    return True

def step(g, m, n):
    primes = []
    for numb in range(m,n):
        if is_prime(numb) and (numb - g) in primes:
            return [numb - g, numb]
        elif is_prime(numb):
            primes.append(numb)
    return None
