"""https://www.codewars.com/kata/52fea6fd158f0576b8000089"""

class Converter():
    
    @staticmethod
    def to_ascii(h):
        hx = [h[i:i+2] for i in range(0,len(h), 2)]
        return ''.join(list(map(lambda x: chr(int(x, 16)), hx)))
        
    @staticmethod
    def to_hex(s):
        return ''.join([hex(ord(i))[2:] for i in s])
