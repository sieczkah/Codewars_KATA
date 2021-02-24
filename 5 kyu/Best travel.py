"""https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python"""


import itertools

def choose_best_sum(t, k, ls):
    comb_list = [i for i in map(sum, itertools.combinations(ls, k)) if i <= t]
    return max(comb_list) if comb_list else None
