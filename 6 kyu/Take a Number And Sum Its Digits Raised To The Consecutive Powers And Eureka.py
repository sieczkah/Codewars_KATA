"""https://www.codewars.com/kata/5626b561280a42ecc50000d1"""


def sum_dig_pow(a, b):
    numbers = []
    for number in range(a, b + 1):
        digits = enumerate([int(i) for i in str(number)], 1)
        digit_sum = sum(num ** place for place, num in digits)
        if digit_sum == number:
            numbers.append(number)
    return numbers
