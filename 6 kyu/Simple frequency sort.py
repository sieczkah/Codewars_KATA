"""https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc"""

def solve(arr):
    return sorted(arr, key= lambda x: (-arr.count(x), x))
