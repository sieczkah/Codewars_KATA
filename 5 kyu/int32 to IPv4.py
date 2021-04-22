"""https://www.codewars.com/kata/52e88b39ffb6ac53a400022e"""

def int32_to_ip(int32):
    binary = bin(int32)[2:].zfill(32)
    ip_bin = [binary[i: i + 8] for i in range(0, 32, 8)]
    return '.'.join(map(lambda x: str(int(x, 2)), ip_bin))
