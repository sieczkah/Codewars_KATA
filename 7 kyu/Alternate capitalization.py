"""https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/python"""

def capitalize(s):
    case1 = ''.join([s[i] if i % 2 else s[i].upper() for i in range(len(s))])
    case2 = case1.swapcase()
    return [case1, case2]
