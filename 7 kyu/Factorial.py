"""https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python"""

def factorial(n):
    if n > 12 or n < 0:
        raise ValueError()
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
