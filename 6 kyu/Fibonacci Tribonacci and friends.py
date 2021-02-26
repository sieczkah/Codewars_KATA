"""https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/python"""


def Xbonacci(signature,n):
    lngth = len(signature)
    if n == 0:
        return []
    elif n < lngth:
        return signature[:n]
    else:
        for _ in range(n-lngth):
            signature.append(sum(signature[-lngth:]))
        return signature
