"""https://www.codewars.com/kata/55b3425df71c1201a800009c/train/python"""


import re


def format_hms(seconds):
    hours = seconds // 3600
    mins = seconds // 60 % 60
    sec = seconds % 60
    return '{:02d}|{:02d}|{:02d}'.format(int(hours), int(mins), int(sec))


def stat(strg):
    if not strg:
        return ""
    result_list = [list(map(int, i.split('|'))) for i in re.findall(r'\d+\|\d+\|\d+', strg)]
    result_secs = [i[0] * 3600 + i[1] * 60 + i[2] for i in result_list]
    lnght = len(result_secs)

    rnge = max(result_secs) - min(result_secs)
    avg = sum(result_secs) / lnght
    if lnght % 2:
        median = sorted(result_secs)[lnght // 2]
    else:
        median = sum(sorted(result_secs)[(lnght // 2) - 1:(lnght // 2) + 1]) / 2

    return f'Range: {format_hms(rnge)} Average: {format_hms(avg)} Median: {format_hms(median)}'

