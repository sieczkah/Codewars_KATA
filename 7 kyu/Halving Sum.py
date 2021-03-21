"""https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d"""

def halving_sum(n): 
    sums = []
    div = 1
    while n // div >= 2:
        sums.append(n // div)
        div *= 2
    return sum(sums) + 1
