"""https://www.codewars.com/kata/5b4070144d7d8bbfe7000001"""

def numericals(s):
    alpha = {letter: 1 for letter in set(s)}
    strng = ''
    for let in s:
        strng += str(alpha[let])
        alpha[let] += 1
    return strng
