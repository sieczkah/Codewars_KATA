"""https://www.codewars.com/kata/526d42b6526963598d0004db"""

from string import ascii_lowercase as LETTERS

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift

    def encode(self, st):
        msg = ''
        for s in st.lower():
            if s in LETTERS:
                msg += LETTERS[(LETTERS.find(s) + self.shift) % 26]
            else:
                msg += s
        return msg.upper()
        
    def decode(self, st):
        msg = ''
        for s in st.lower():
            if s in LETTERS:
                msg += LETTERS[(LETTERS.find(s) - self.shift) % 26]
            else:
                msg += s
        return msg.upper()
