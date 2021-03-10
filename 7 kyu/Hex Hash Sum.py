"""https://www.codewars.com/kata/5ab363ff6a176b29880000dd/train/python"""

def hex_hash(code):
    char = ''.join([hex(ord(i)) for i in code])
    return sum(int(numb) for numb in char if numb.isdigit())
