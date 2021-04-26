"""https://www.codewars.com/kata/55c6126177c9441a570000cc"""

def order_weight(strng):
    weights = strng.split()
    wofw = list(map(lambda x: sum(int(i) for i in x), weights))
    weight_list = sorted(list(zip(wofw, weights)), key=lambda x: (x[0], x[1]))
    return ' '.join(weight for _, weight in weight_list)
