"""https://www.codewars.com/kata/55d5434f269c0c3f1b000058"""


def triple_double(num1, num2):
    numb = '0123456789'
    for i in numb:
        if i * 3 in str(num1):
            numb = i
    return 1 if numb * 2 in str(num2) else 0

