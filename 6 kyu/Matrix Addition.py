"""https://www.codewars.com/kata/526233aefd4764272800036f"""

def matrix_addition(a, b):
    result = [[a[r][c] + b[r][c] for c in range(len(a))] for r in range(len(a))]
    return result
