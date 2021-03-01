"""https://www.codewars.com/kata/602afedfd4a64d0008eb4e6e/python"""


def get_day(day, is_leap):
    year = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31,
            'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31,
            'November': 30, 'December': 31}
    if is_leap:
        year['February'] += 1
    for m in year.keys():
        if day > year[m]:
            day -= year[m]
        else:
            break
    return f'{m}, {day}'
