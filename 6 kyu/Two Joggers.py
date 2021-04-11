"""https://www.codewars.com/kata/5274d9d3ebc3030802000165"""

def smallest_multiple(a, b):
    x, y = a, b
    while b:
        a, b = b, a%b
    return x * y / a

def nbr_of_laps(x, y):
    if x == y:
        return (1,1)
    else:
        mult = smallest_multiple(x, y)
        return (mult // x , mult // y)
