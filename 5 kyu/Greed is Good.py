"""https://www.codewars.com/kata/5270d0d18625160ada0000e4"""

score_3x = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
score_1x = {1: 100, 5: 50}

def score(dice):
    triplets = []
    rest = []
    for i in dice:
        if dice.count(i) > 2 and triplets.count(i) != 3:
            triplets.append(i)
        elif i in [1, 5]:
            rest.append(i)
    score = 0
    if triplets:
        score += score_3x[triplets[0]]
    return sum(score_1x[i] for i in rest) + score
