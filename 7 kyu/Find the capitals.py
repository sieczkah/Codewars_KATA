"""https://www.codewars.com/kata/539ee3b6757843632d00026b/train/python"""


def capitals(word):
     return [ind for ind, letter in enumerate(word) if letter.isupper()]

