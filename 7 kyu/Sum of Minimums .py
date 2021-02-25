"""https://www.codewars.com/kata/5d5ee4c35162d9001af7d699/train/python"""


def sum_of_minimums(numbers):
    return sum(min(i) for i in numbers)
