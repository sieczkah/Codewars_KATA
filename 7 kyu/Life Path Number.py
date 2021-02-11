"""https://www.codewars.com/kata/5a1a76c8a7ad6aa26a0007a0/train/python"""

def reduce(number):
    if number < 10:
        return number
    else:
        x = sum(int(i) for i in str(number))
        return reduce(x)


def life_path_number(birthdate):
    birth = [reduce(i) for i in map(int, birthdate.split('-'))]
    return reduce(sum(birth))
