"""https://www.codewars.com/kata/5a946d9fba1bb5135100007c"""

from math import sqrt

def is_prime(numb):
    if numb < 2:
        return False
    else:
        for i in range(2, int(sqrt(numb)) + 1):
            if numb % i == 0:
                return False
        return True

def minimum_number(numbers):
    el_sum = sum(numbers)
    while not is_prime(el_sum):
        el_sum += 1
    return el_sum - sum(numbers)

