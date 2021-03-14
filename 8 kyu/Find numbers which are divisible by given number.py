"""https://www.codewars.com/kata/55edaba99da3a9c84000003b"""

def divisible_by(numbers, divisor):
    return [i for i in numbers if i % divisor == 0]
