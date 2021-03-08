"""https://www.codewars.com/kata/59859f435f5d18ede7000050/train/python"""

def word_to_bin(word):
    return [bin(i)[2:].zfill(8) for i in map(ord, list(word))]
