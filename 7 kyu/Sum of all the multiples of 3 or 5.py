"""https://www.codewars.com/kata/57f36495c0bb25ecf50000e7/train/python"""

def find(n):
    return sum(i for i in range(n+1) if not i % 5 or not i % 3)
