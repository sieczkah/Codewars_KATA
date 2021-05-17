"""https://www.codewars.com/kata/590adadea658017d90000039"""


def fruit(reels, spins):
    score_board = {'Wild': 10, 'Star': 9, 'Bell': 8, 'Shell': 7, 'Seven': 6,
                   'Cherry': 5, 'Bar': 4, 'King': 3, 'Queen': 2, 'Jack': 1}
    spined = [reel[spin] for reel, spin in zip(reels, spins)]

    if len(set(spined)) == 1:
        return score_board[spined[0]] * 10
    elif len(set(spined)) == 2:
        dbl = sorted(spined, key=lambda x: -spined.count(x))[0]
        scr = score_board[dbl]
        return scr * 2 if spined.count('Wild') == 1 else scr
    return 0
