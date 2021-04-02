"""https://www.codewars.com/kata/523a86aa4230ebb5420001e1"""


def anagrams(word, words):
    anagrams_list = [i for i in words if sorted(i) == sorted(word)]
    return anagrams_list
