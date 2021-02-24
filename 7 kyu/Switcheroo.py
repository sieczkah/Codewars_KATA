"""https://www.codewars.com/kata/57f759bb664021a30300007d/solutions/python/following/best_practice"""


def switcheroo(string):
    d = { 97: 98, 98: 97} # 
    return string.translate(d)

# Alternate solution
# def switcheroo(string):
#     d = { 'a': 'b', 'b': 'a', 'c':'c'}
#     return ''.join(d[i] for i in string)
