"""https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e"""

def flip_filter(grp):
    return '0' if grp.count('0') > grp.count('1') else '1'

def encode(string):
    bit_str = ''.join(bin(ord(i))[2:].zfill(8) for i in string)
    return ''.join(list(map(lambda x : x*3, bit_str)))

def decode(bits):
    bit_str = ''.join([flip_filter(bits[i:i+3]) for i in range(0, len(bits), 3)])
    msg = ''
    for i in range(0, len(bit_str), 8):
        msg += chr((int(bit_str[i:i+8], 2)))
    return msg
