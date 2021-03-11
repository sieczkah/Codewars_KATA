"""https://www.codewars.com/kata/568d0dd208ee69389d000016"""

def rental_car_cost(d):
    if d < 3:
        return d * 40
    else:
        return d * 40 - 50 if d >= 7 else d * 40 - 20
