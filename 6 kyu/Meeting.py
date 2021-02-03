"""https://www.codewars.com/kata/59df2f8f08c6cec835000012"""


def meeting(s):
    guest_list = []
    for name, surname in [x.split(':') for x in s.upper().split(';')]:
        guest_list.append(f'({surname}, {name})')
    return ''.join(sorted(guest_list))
