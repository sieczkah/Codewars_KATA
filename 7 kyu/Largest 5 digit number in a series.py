"""https://www.codewars.com/kata/51675d17e0c1bed195000001"""


def solution(digits):
    biggest = 0
    if len(digits) > 5:
        for i in range(len(digits)):
            if int(digits[i:i + 5]) > biggest:
                biggest = int(digits[i:i + 5])
    return biggest
