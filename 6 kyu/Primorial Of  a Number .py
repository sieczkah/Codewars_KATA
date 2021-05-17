"""https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124"""

def is_prime(n):
    for div in range(2, int(n ** 0.5) + 1):
        if n % div == 0:
            return False
    return True

def num_primorial(n):
    cur_prime = 2
    primorial = 1
    while n != 0:
        if is_prime(cur_prime):
            primorial *= cur_prime
            n -= 1
        cur_prime += 1
    return primorial
