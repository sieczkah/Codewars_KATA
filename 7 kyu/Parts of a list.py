"""https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python"""

def partlist(arr):
    posibl = []
    for i in range(len(arr)- 1):
        suf = ' '.join(arr[:i+1])
        pref = ' '.join(arr[i+1:])
        posibl.append((suf, pref))
    return posibl
