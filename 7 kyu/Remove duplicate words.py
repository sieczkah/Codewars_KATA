"""https://www.codewars.com/kata/5b39e3772ae7545f650000fc/solutions/python/me/best_practice"""

def remove_duplicate_words(s):
    words = []
    for i in s.split():
        if i not in words:
            words.append(i)
    return ' '.join(words)
