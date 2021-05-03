"""https://www.codewars.com/kata/5966847f4025872c7d00015b"""

str_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
             'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
num_to_str = {n:s for s, n in str_to_num.items()}

def average_string(s):
    numbers = [str_to_num.get(str_num, 'n/a') for str_num in s.split()]
    if 'n/a' in numbers or len(s) == 0:
        return 'n/a'
    return num_to_str[(sum(numbers) // len(numbers))]
