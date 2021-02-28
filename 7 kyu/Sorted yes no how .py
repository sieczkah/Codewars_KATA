"""https://www.codewars.com/kata/580a4734d6df748060000045/train/python"""


def is_sorted_and_how(arr):
    sort_check = [arr[i] <= arr[i + 1] for i in range(len(arr) - 1)]
    if len(set(sort_check)) == 1:
        return 'yes, ascending' if all(sort_check) else 'yes, descending'
    else:
        return 'no'
