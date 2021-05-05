"""https://www.codewars.com/kata/52b305bec65ea40fe90007a7"""

def grabscrab(word, possible_words):
    return [w for w in possible_words if sorted(w) == sorted(word)]
