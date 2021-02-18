"""https://www.codewars.com/kata/545cedaa9943f7fe7b000048"""


import string

def is_pangram(s):
    letters = set([l.lower() for l in s if l.isalpha()])
    return ''.join(sorted(letters)) in string.ascii_lowercase
