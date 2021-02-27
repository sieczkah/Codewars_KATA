"""https://www.codewars.com/kata/51e0007c1f9378fa810002a9/python"""


def parse(data):
    val = 0
    ret_arr = []
    for letter in data:
        if letter == 'i':
            val += 1
        elif letter == 'd':
            val -= 1
        elif letter == 's':
            val *= val
        elif letter == 'o':
            ret_arr.append(val)
    return ret_arr
