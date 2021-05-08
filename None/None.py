"""None"""

import math

def is_prime(n):
    if n in [0, 1]:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 and n != i:
            return False
    return True
    
def prime(n):
    primes = [x for x in range(n + 1) if is_prime(x)]
    return primes
