"""https://www.codewars.com/kata/52dca71390c32d8fb900002b"""

def number_to_ordinal(n):
    suf = {'1': 'st', '2':'nd', '3': 'rd'}
    s = str(n)
    if n == 0:
        return s
    else:
        if n > 10 and s[-2:] in ['11','12','13']:
            return s + 'th'
        else:
            return s + suf.get(s[-1], 'th')
