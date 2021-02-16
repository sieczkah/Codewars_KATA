"""https://www.codewars.com/kata/58693136b98de0e4910001ab/train/python"""


from string import ascii_lowercase

def decrypt(test_key):
    return "".join(str(test_key.count(char)) for char in ascii_lowercase)
