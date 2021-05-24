"""https://www.codewars.com/kata/57d165ad95497ea150000020"""

pairs = {'B': '8', '8':'B'}
def bears(x,s):
    mat, cur = '', ''
    for b in s:
        if pairs.get(b, None) == cur:
            mat += cur + b
            cur = ''
        else:
            cur = b
    return [mat, len(mat) >= x] 
