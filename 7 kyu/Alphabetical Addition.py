"""https://www.codewars.com/kata/5d50e3914861a500121e1958/train/python"""


from string import ascii_lowercase as asc

def add_letters(*letters):
    if letters:
        lett_sum = sum(asc.find(i) + 1 for i in letters) % 26
        return asc[lett_sum - 1]
    else:
        return 'z'
