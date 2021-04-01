"""https://www.codewars.com/kata/598106cb34e205e074000031"""

def count_deaf_rats(town):
    t = town.replace(' ', '')
    pip = t.find('P')
    left = [t[i] + t[i+1] for i in range(0, pip, 2)]
    right = [t[i] + t[i+1] for i in range(pip + 1, len(t), 2)]
    return left.count('O~') + right.count('~O')

