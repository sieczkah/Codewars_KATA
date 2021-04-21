"""https://www.codewars.com/kata/5539fecef69c483c5a000015"""

import math

def is_prime(num):
    for i in range(2, round(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
                       
def backwards_prime(start, stop):
    primes = [num for num in range(start, stop +1) if is_prime(num)]
    back_primes = []
    for prime in primes:
        back_p = int(str(prime)[::-1])
        # checking if prime backwards is prime and it's not a palindrome
        if is_prime(back_p) and back_p != prime:
            back_primes.append(prime)
    return back_primes
