"""https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/train/python"""

def up_array(arr):
    if not arr or any([i > 9 or i < 0 for i in arr]):
        return None
    else:
        number = int(''.join(map(str, arr))) + 1
        return [int(i) for i in str(number)]

