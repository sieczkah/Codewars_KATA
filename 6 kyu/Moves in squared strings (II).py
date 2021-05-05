"""https://www.codewars.com/kata/56dbe7f113c2f63570000b86"""

def rot(strng):
    return '\n'.join(s[::-1] for s in strng.split('\n')[::-1])
def selfie_and_rot(strng):
    dot = '.' * len(strng.split('\n')[0])
    return strng.replace('\n', f'{dot}\n') + f'{dot}\n{dot}'  + rot(strng).replace('\n', f'\n{dot}')
def oper(fct, s):
    return fct(s)
