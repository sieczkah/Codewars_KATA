"""https://www.codewars.com/kata/52945ce49bb38560fe0001d9"""

def pascal(p):
    tri = []
    for j in range(p):
        line = []
        for k in range(j + 1):
            if k == 0 or k == j:
                line.append(1)
            else:
                line.append(tri[j-1][k-1] + tri[j-1][k])
        tri.append(line)
    return tri
                
