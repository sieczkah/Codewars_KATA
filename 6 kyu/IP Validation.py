"""https://www.codewars.com/kata/515decfd9dcfc23bb6000006"""


def is_valid_IP(strng):
    ip = strng.split('.')
    if not all(i.isdigit() for i in ip):
        return False
    valid1 = [0 <= int(i) <= 255 for i in ip]
    valid2 = [not i.startswith('0') for i in ip if int(i) != 0]
    return len(ip) == 4 and all(valid1 + valid2)
