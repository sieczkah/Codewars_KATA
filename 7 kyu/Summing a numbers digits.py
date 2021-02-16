"""https://www.codewars.com/kata/52f3149496de55aded000410/solutions/python/me/best_practice"""


def sum_digits(number):
    a = abs(number)
    return sum(int(i) for i in str(a))
