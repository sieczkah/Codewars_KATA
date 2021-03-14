"""https://www.codewars.com/kata/57f6ad55cca6e045d2000627"""

def square_or_square_root(arr):
    return [int(i ** 0.5) if (i ** 0.5).is_integer() else i ** 2 for i in arr]
