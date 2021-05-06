"""https://www.codewars.com/kata/559ce00b70041bc7b600013d"""

def finance(n):
    # every week is an arithmetic sequance with step = 1
    # starting with start and having the length of n-1 every week
    start = 0
    money = 0
    for i in range(n + 1, 0, -1):
        # see arithmetic sequance sum and nth element
        money +=  (2 * start + i - 1) / 2 * i
        start += 2
    return money

