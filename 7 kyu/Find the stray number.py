"""https://www.codewars.com/kata/57f609022f4d534f05000024"""

def stray(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            number = i
    return number