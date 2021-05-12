"""https://www.codewars.com/kata/5946a0a64a2c5b596500019a"""

def split_and_add(numbers, n):
    for _ in range(n):
        mid = len(numbers) // 2
        if len(numbers) % 2 == 0:
            numbers = [sum(i) for i in zip(numbers[:mid], numbers[mid:])]
        else:
            numbers = [numbers[mid]] +[sum(i) for i in zip(numbers[:mid], numbers[mid + 1:])]
    return numbers
