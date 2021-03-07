"""https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python"""

def highest_rank(arr):
    no = None
    count = 0
    for i in sorted(set(arr), reverse=True):
        cnt = arr.count(i)
        if cnt > count:
            no = i
            count = cnt
    return no

