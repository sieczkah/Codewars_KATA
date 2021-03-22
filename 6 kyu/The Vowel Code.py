"""https://www.codewars.com/kata/53697be005f803751e0015aa"""

c = {'a': '1', 'e': '2', 'i':'3', 'o': '4', 'u': '5'}
dc = {'1': 'a', '2': 'e', '3':'i', '4': 'o', '5': 'u'}
def encode(st):
    return ''.join([c[i] if i in c.keys() else i for i in st])
    
def decode(st):
    return ''.join([dc[i] if i in dc.keys() else i for i in st])
