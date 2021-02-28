"""https://www.codewars.com/kata/5aff237c578a14752d0035ae/train/python"""


def predict_age(*ages):
    return (sum(map(lambda x: x ** 2, ages)) ** 0.5) // 2
