"""https://www.codewars.com/kata/52eb114b2d55f0e69800078d"""

class Cipher(object):
    def __init__(self, map1, map2):
        self.encode_map = {key: item for key, item in zip(map1, map2)}
        self.decode_map = {item: key for key, item in zip(map1, map2)}
    
    def encode(self, s):
        return ''.join(self.encode_map.get(i, i) for i in s)
    
    def decode(self, s):
        return ''.join(self.decode_map.get(i, i) for i in s)
