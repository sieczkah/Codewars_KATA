"""https://www.codewars.com/kata/51b62bf6a9c58071c600001b"""


def solution(n):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman = ''
    i = 0
    while n > 0:
        for _ in range(n // values[i]):
            roman += symbols[i]
            n -= values[i]
        i += 1
    return roman
