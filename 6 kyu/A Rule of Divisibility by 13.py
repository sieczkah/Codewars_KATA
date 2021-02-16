"""https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/python"""


remainders = [1, 10, 9, 12, 3, 4]

def thirt(n):
    num_n = [int(i) for i in str(n)][::-1]
    seq = sum(num_n[i] * remainders[i % 6] for i in range(len(num_n)))
    if seq != n:
        return thirt(seq)
    else:
        return seq
