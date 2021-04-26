"""https://www.codewars.com/kata/5616868c81a0f281e500005c"""

from string import ascii_lowercase as asc


def name_val(name, weight):
    return (sum(asc.find(letter) + 1 for letter in name.lower()) + len(name)) * weight


def rank(st, we, n):
    # if enought participants
    if st and n <= len(we):
        names = st.split(',')
        ranks = [name_val(name, wght) for name, wght in zip(names, we)]
        name_rank = sorted(zip(names, ranks), key=lambda x: (-x[1], x[0]))
        return name_rank[n - 1][0]
    return 'Not enough participants' if st else 'No participants'
