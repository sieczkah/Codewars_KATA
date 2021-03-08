"""https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python"""

def first_non_repeating_letter(string):
    non_repeat = [i for i in string if string.lower().count(i.lower()) == 1]
    return non_repeat[0] if non_repeat else ""
