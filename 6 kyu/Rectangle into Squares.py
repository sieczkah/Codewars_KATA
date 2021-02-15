"""https://www.codewars.com/kata/55466989aeecab5aac00003e/solutions/python/me/best_practices"""


def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    results = []
    while lng != wdth:
        if lng > wdth:
            lng -= wdth
            results.append(wdth)
        elif wdth > lng:
            wdth -= lng
            results.append(lng)
    results.append(wdth)
    return results
