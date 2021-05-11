"""https://www.codewars.com/kata/53e895e28f9e66a56900011a"""

from string import ascii_lowercase as let

def letter_frequency(text):
    text = text.lower()
    return sorted([(i, text.count(i)) for i in set(text) if i in let], key=lambda x: (-x[1], x[0]))    
