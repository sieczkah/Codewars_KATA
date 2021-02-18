"""https://www.codewars.com/kata/51b6249c4612257ac0000005"""


def solution(roman):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    liczba = 0
    while roman:
        for i in symbols:
            if roman.startswith(i):
                liczba += values[symbols.index(i)]
                roman = roman[len(i):]
    return liczba
