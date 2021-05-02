"""https://www.codewars.com/kata/5583d268479559400d000064"""

def binary_to_string(binary):
    bit_list = [binary[i: i + 8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(bit, 2)) for bit in bit_list)
