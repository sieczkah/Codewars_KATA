"""https://www.codewars.com/kata/5663f5305102699bad000056"""

def minmaxlen(arr):
    len_arr = [len(i) for i in arr]
    return min(len_arr), max(len_arr)

def mxdiflg(a1, a2):
    if a1 == [] or a2 == []:
        return -1
    min_a1, max_a1 = minmaxlen(a1)
    min_a2, max_a2 = minmaxlen(a2)
    return max([max_a2 - min_a1, max_a1 - min_a2])
