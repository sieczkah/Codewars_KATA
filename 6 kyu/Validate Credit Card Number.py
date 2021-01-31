"""https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2/python"""


def validate(n):
    numbers = [int(n) for n in str(n)]
    for i in range(1, len(numbers) + 1):
        if not i % 2:
            x = numbers[-i] * 2
            if x > 9:
                x = x - 9
            numbers[-i] = x

    return False if sum(numbers) % 10 else True
