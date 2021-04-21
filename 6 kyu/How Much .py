"""https://www.codewars.com/kata/55b4d87a3766d9873a0000d4"""

def howmuch(m, n):
    j, k = sorted([m, n])
    fortune = []
    for i in range(j, k + 1):
        if (i - 1) % 9 == 0 and (i - 2) % 7 == 0:
            fortune.append([f'M: {i}',
                            f'B: {(i - 2) // 7}',
                            f'C: {(i - 1) // 9}'])
    return fortune


