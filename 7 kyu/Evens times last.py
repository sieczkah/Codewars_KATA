"""https://www.codewars.com/kata/5a1a9e5032b8b98477000004"""

def even_last(numbers): 
    return sum(numbers[::2]) * numbers[-1] if numbers else 0
