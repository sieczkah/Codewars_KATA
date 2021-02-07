"""https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python"""


def make_readable(seconds):
    time = [seconds // 3600, seconds % 3600 // 60, seconds % 60]
    return ':'.join([str(i).zfill(2) for i in time])
