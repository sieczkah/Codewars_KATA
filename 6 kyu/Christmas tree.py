"""https://www.codewars.com/kata/52755006cc238fcae70000ed"""

def arit(n):
    # returns arithmetic sequence nth element
    return 1 + (n - 1) * 2

def christmas_tree(height):
    tree = []
    for i in range(1, height + 1):
        branch = '*' * arit(i)
        space = ' ' * ((arit(height) - len(branch)) // 2)
        tree.append(space + branch + space)
    return '\n'.join(tree)
