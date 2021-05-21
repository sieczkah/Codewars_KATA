"""https://www.codewars.com/kata/5631ac5139795b281d00007d"""

import re

class WordDictionary:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def search(self, pattern):
        pat = re.compile(f'^{pattern}$')
        return True if list(filter(pat.match, self.words)) else False
