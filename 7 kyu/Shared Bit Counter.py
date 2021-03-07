"""https://www.codewars.com/kata/58a5aeb893b79949eb0000f1/train/python"""

def shared_bits(a, b):
    # binary & operand copies a bit if it exists in both numbers
    return bin(a & b).count('1') > 1
