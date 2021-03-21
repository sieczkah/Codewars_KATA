"""https://www.codewars.com/kata/52ea928a1ef5cfec800003ee"""

def ip_to_int32(ip):
    # Split string by dot so we get the octets
    # Convert octec from string -> int -> binary
    # Binary in python is reprsented by 0b.... so we ignore 2 first characters with slice :2
    # with zfill we are filling empty bits up to 8
    # join the list of bits and with int convert them from binary to decimal
    bin_ip = [bin(int(i))[2:].zfill(8) for i in ip.split('.')]
    return int(''.join(bin_ip), 2)
