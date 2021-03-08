"""https://www.codewars.com/kata/53907ac3cd51b69f790006c5/train/python"""

# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    s1, s2, lng = sorted([a, b, c])
    if lng >= s1 + s2:
        return 0
    cosa = (s1** 2 + s2 ** 2 - lng ** 2)/ (2 * s1 * s2)
    if cosa == 0:
        return 2
    else:
        return 1 if cosa > 0 else 3
