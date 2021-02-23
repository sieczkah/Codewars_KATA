"""https://www.codewars.com/kata/5226eb40316b56c8d500030f/train/python"""


from math import factorial 

def pascals_triangle(n):
    row_list = []
    for r in range(n):
        for c in range(r + 1):
            no = factorial(r)//(factorial(c)*factorial(r-c))
            row_list.append(no)
    return row_list
