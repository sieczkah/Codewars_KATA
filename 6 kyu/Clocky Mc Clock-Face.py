"""https://www.codewars.com/kata/59752e1f064d1261cb0000ec"""

def what_time_is_it(angle):
    mins = int(angle * 2)
    hour, min = mins // 60 % 12, mins % 60
    if hour == 0: hour = 12
    return f'{hour}'.zfill(2) + ':' + f'{min}'.zfill(2)
