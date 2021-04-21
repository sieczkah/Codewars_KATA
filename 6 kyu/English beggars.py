"""https://www.codewars.com/kata/59590976838112bfea0000fa"""

def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]
