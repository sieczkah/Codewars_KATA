"""https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python"""


def packValues(subList):
    if len(subList) > 2:
        return f'{subList[0]}-{subList[-1]}'
    return ','.join(map(str, subList))

def solution(args):
    grouped = []
    stack = []
    for i in args:
        print(i)
        print(stack)
        if not stack:
            stack = [i]
        else:
            if stack[-1] + 1 == i:
                stack.append(i)
            else:
                grouped.append(packValues(stack))
                stack = [i]
    grouped.append(packValues(stack))
    return ','.join(grouped)
