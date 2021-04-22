"""https://www.codewars.com/kata/525dfedb5b62f6954d000006"""

def score_throws(radii):
    if not radii:
        return 0
    score = sum(10 if rad < 5 else 5 for rad in filter(lambda x: x <=10, radii))
    return score + 100 if score == len(radii) * 10 else score
