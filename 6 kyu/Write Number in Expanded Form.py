"""https://www.codewars.com/kata/5842df8ccbd22792a4000245"""


def expanded_form(num):
    numbers = []
    fill = len(str(num))
    for i in list(str(num)):
        if i != '0':
            numbers.append(i.zfill(fill)[::-1])
        fill -= 1
    return ' + '.join(numbers)
