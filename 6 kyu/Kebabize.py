"""https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python"""

from string import ascii_lowercase as as_low
from string import ascii_uppercase as as_up
import re

def kebabize(string):
    string = re.sub(r'[^A-Za-z]', '', string)
    words = [i if i in as_low else '-' + i.lower() for i in string]
    return ''.join(words).strip('-')
