"""https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/python"""


def evaporator(content, evap_per_day, threshold):
    x = 100
    d = 0
    while x > threshold:
        x -= x * evap_per_day / 100
        d +=1
    return d
