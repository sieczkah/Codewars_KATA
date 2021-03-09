"""https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/python"""

def sum_triangular_numbers(n):
    x = 0
    sums = 0
    for i in range(1, n+1):
        sums += i + x
        x = i + x
    return sums
# the end value of a row is the number of the row + value of previous row
# Considering Tetrahefral number definition 
# https://en.wikipedia.org/wiki/Tetrahedral_number
# We can also make it as:
def sum_triangular_numbers(n):
    return n * (n + 1) * (n + 2) / 6 if n > 0 else 0
